#!python
from datastore import get_entries_by_title
from compare_docs import tokenize, similarity

import re

# get entries by title
#TODO: needs generic titles
title = 'Nanjing Massacre'
entry = get_entries_by_title(title)

# find the lsa score against English that is the farthest
langs = [lang for lang in entry['language'].keys()]
lsa_scores = [lang_dict['LSA_score'] 
                for lang, lang_dict in entry['language'].items()]
scores = list(zip(langs, lsa_scores))
farthest_lang = sorted(scores, key=lambda x: x[1])[0][0]

# get that language's translation text
farthest_lang_text = entry['language'][farthest_lang]['translated_content']

# cut it up into sentences
sentences = re.split(r'[?!.]', farthest_lang_text) # \n
sentences = [sentence for sentence in sentences if len(sentence) > 5]

#TODO: is it possible to get rid of empty token spots while retainig the order?
tokenized_sentences = [tokenize(sentence) for sentence in sentences] # some empty results...need to see if that is problematic.

# prep the english version of the content:
english_entry = entry['content']
tokenized_english_entry = tokenize(english_entry)

# run each sentence in the forn doc on the english LSA for similarity.
# should be a list of sentences with the least content in common, to map to 'sentences'
documents = ([tokenized_english_entry] + tokenized_sentences)

# sort, retaining the order number. Realize that 0 is the english document.
similarities = list(similarity(documents))[1:]
least_common_content = sorted(enumerate(similarities), 
                              key=lambda x: list(x)[1])
least_common_content = [item for item in least_common_content if item[1] != 0.0]

# TODO: return the n farthest sentences based on the ratio of original distance.
print(title)
print("Language edition's article farthest from the English version: ",farthest_lang)
print()
for index, score in least_common_content[:25]:
    print(score)
    print(sentences[index])
    #print(tokenized_sentences[index])
    print()

'''
different_content = [sentences[index] for index, score in least_common_content
                                if len(sentences[index]) > 15][:25]
'''