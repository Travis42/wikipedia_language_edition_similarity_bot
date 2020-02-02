#!python
from datastore import get_all_titles_from_db, get_entries_by_title
from compare_docs import tokenize, similarity
from utils import moveToSubfolder

import re

# get entries by title
titles = get_all_titles_from_db()
for title in titles:
    title = title[0]
    entry = get_entries_by_title(title)

    # find the lsa score against English that is the farthest
    langs = [lang for lang in entry['language'].keys()]
    lsa_scores = [lang_dict['LSA_score'] 
                    for lang, lang_dict in entry['language'].items()]
    scores = list(zip(langs, lsa_scores))
    try:
        farthest_lang = sorted(scores, key=lambda x: x[1])[0][0]
    except (IndexError, TypeError):
        print(scores)
        print('skipping for now.  See why its wrong!: ', title)
        continue

    # get that language's translation text
    farthest_lang_text = entry['language'][farthest_lang]['translated_content']

    # cut it up into sentences
    sentences = re.split(r'[?!.。]\s+', farthest_lang_text) #r'[?!.。]\s+'
    sentences = [sentence for sentence in sentences if len(sentence) > 5]

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
    least_common_content = [item for item in least_common_content 
                                    if item[1] != 0.0 and item[1] <= 0.3]

    # TODO: return the n farthest sentences based on the ratio of original distance.
    with open(title + "_results.txt", "w") as f:
        f.write(title)
        f.write('\n')
        f.write("Language edition's article farthest from the English version: ")
        f.write(farthest_lang)
        f.write('\n')
        for index, score in least_common_content:
            f.write(str(score))
            f.write('\n')
            f.write(sentences[index])
            #f.write(tokenized_sentences[index])
            f.write('\n')

    moveToSubfolder('results', title + "_results.txt")