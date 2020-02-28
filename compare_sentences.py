#!python
from compare_docs import tokenize, similarity
from datastore import get_all_titles_from_db, get_entries_by_title
from utils import moveToSubfolder

import configparser
import re


def turn_doc_into_sentences(document):
    # cut it up into sentences
    sentences = re.split(r'[?!.。][\s+[]', document) #r'[?!.。]\s+'
    return [sentence for sentence in sentences if len(sentence) > 5]


def write_sentence_comparisons_to_file(title, primary_lang, comparison_lang,
                                         least_common_content, sentences):
    file_name = title + '_' + primary_lang + '_edition_differences_w_' + \
                comparison_lang + "_edition.txt"
    with open(file_name, "w") as f:
        f.write('How to read this document: ')
        f.write("Passages from one language's article appear in order of their likelihood of containing different content from the other language.")
        f.write(" The further down you read, the more likely that the content between languages is similar.")
        f.write(" If the list is short, it is likely that the content between languages is highly similar, or that the original language article for this subject is not very long.")
        f.write(" Passages may be from any part of an article.  Sometimes they are captions for pictures, sometimes references, and sometimes they are part of the article itself.")
        f.write(" Not every passage will be meaningful.  This is merely a guide to help you find the most novel content, quickly.")
        f.write("\n")
        f.write("\n")
        f.write(title)
        f.write('\n')
        f.write('\n')
        f.write(primary_lang)
        f.write(" edition's differences with the ")
        f.write(comparison_lang + " version: ")
        f.write('\n')
        f.write('\n')
        number = 1
        for index, score in least_common_content:
            f.write('\n')
            f.write(str(number))
            number += 1
            f.write('. ')
            f.write('\n')
            f.write(sentences[index])
            f.write('. ')
            #f.write(tokenized_sentences[index])
            f.write('\n')

    moveToSubfolder('results', file_name)


config = configparser.ConfigParser()
config.read("config.cnf")
primary_lang = config.get('Primary_Language', 'primary_language')

# get entries by title
titles = get_all_titles_from_db()
for title in titles:
    title = title[0]
    entry = get_entries_by_title(title)

    # prep the english version of the content:
    english_entry = entry['content']
    if english_entry:
        tokenized_english_entry = tokenize(english_entry)
    else:
        continue

    # find the lsa score against English that is the most different
    langs = [lang for lang in entry['language'].keys()]
    lsa_scores = [lang_dict['LSA_score'] 
                    for lang, lang_dict in entry['language'].items()]
    scores = list(zip(langs, lsa_scores))
    try:
        farthest_lang = sorted(scores, key=lambda x: x[1])[0][0]
    except (IndexError, TypeError):
        print(scores)
        print('skipping for now.  See why its wrong!: ', title)
        # its wrong either because article is only in one lang, (IndexError)
        # or because LSA_score saved incorrectly, as a binary. (TypeError)
        continue

    # get that language's translation text
    farthest_lang_text = entry['language'][farthest_lang]['translated_content']








    # cut it up into sentences
    sentences = turn_doc_into_sentences(farthest_lang_text)

    tokenized_sentences = [tokenize(sentence) for sentence in sentences] # some empty results...need to see if that is problematic.

    # run each sentence in the forn doc on the english LSA for similarity.
    # should be a list of sentences with the least content in common, to map to 'sentences'
    documents = ([tokenized_english_entry] + tokenized_sentences)

    # sort, retaining the order number. Realize that 0 is the english document.
    similarities = list(similarity(documents))[1:]
    least_common_content = sorted(enumerate(similarities), 
                                  key=lambda x: list(x)[1])
    least_common_content = [item for item in least_common_content 
                                    if item[1] != 0.0 and item[1] <= 0.3]
    if not least_common_content:
        # article is not sufficiently different
        continue

    write_sentence_comparisons_to_file(title, farthest_lang, primary_lang, 
                                        least_common_content, sentences)






    # now create the opposite result: top novel content in the primary language compared with the foreign language.
    sentences = turn_doc_into_sentences(english_entry)
    tokenized_sentences = [tokenize(sentence) for sentence in sentences]

    # prep the main document to compare against:
    tokenized_lang_entry = tokenize(farthest_lang_text)

    # run each sentence in the En doc on the Forn LSA for similarity.
    # should be a list of sentences with the least content in common, to map to 'sentences'
    documents = ([tokenized_lang_entry] + tokenized_sentences)

    # sort, retaining the order number. Realize that 0 is the english document.
    similarities = list(similarity(documents))[1:]
    least_common_content = sorted(enumerate(similarities), 
                                  key=lambda x: list(x)[1])
    least_common_content = [item for item in least_common_content 
                                    if item[1] != 0.0 and item[1] <= 0.3]
    if not least_common_content:
        # article is not sufficiently different
        continue

    write_sentence_comparisons_to_file(title, primary_lang, farthest_lang,
                                        least_common_content, sentences)
