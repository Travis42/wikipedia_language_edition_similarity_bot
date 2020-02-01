#!python
import datastore
from utils import read_txt_to_string, read_txt_to_string_in_chunks, combine_string_generator_pieces

from gensim import corpora, models, similarities
from nltk import word_tokenize
from nltk.corpus import stopwords

from collections import defaultdict, namedtuple
from copy import deepcopy
import logging
import re
import string
import sys

'''
Note:  I'm assuming that all dicitonaries in Python are now Ordered in terms of insertion order.  This is true for Python 3.6.
'''

def tokenize(document):
    tokenized = document

    tokenized = tokenized.strip().lower()

    # getting rid of punctuation:
    tokenized = re.sub('[' + string.punctuation + ']', '', tokenized)

    # remove English stop words
    stop = stopwords.words('english')
    tokenized = combine_string_generator_pieces((str(word + ' ') for word in tokenized.split() if word not in (stop)))

    # Tokenizing the string w NLTK word_tokenize
    tokenized = word_tokenize(tokenized)

    # remove words that appear only once
    frequency = defaultdict(int)
    for token in tokenized:
        frequency[token] += 1
    tokenized = [token for token in tokenized if frequency[token] > 1]

    # Lemmatization in unncessary for LSA.

    return tokenized


def similarity(documents_list, comparison="lsa"):
    '''
    comparison:  string that shows what kind of NLP process to use.
    '''
    dictionary = corpora.Dictionary(documents_list)
    corpus = [dictionary.doc2bow(text) for text in documents_list]

    if comparison == "lsa":
        nlp = models.LsiModel(corpus, 
                              id2word=dictionary, 
                              num_topics=len(corpus))
    elif comparison == "tfidf":
        nlp = models.TfidfModel(corpus, id2word=dictionary)

    vectorized = nlp[corpus[0]] # first document is our thing to compare against.

    index = similarities.MatrixSimilarity(nlp[corpus])  # transform corpus to vector space and index it
    # Options:
    #index.save('/tmp/deerwester.index')
    #index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
    sims = index[vectorized]  # perform a similarity query against the corpus
    # format: document #, similarity score

    # return similarities least to most
    #sims = sorted(enumerate(sims), key=lambda x: x[1])
    return sims


def compare_docs(topic):
    # all translations:
    documents = [content['translated_content'] for lang, content in topic['language'].items()]

    # add in English
    documents.insert(0, topic['content'])
    logging.info('There are this many documents', len(documents))

    # Tokenize
    tokenized_texts = [tokenize(doc) for doc in documents]

    assert len(documents) == len(tokenized_texts)
    # what goes in ^ should come out, same len.
    for tokens in tokenized_texts:
        assert len(tokens) != 0

    # TODO: fix this to reflect different kinds of similarity studies.
    # Compare
    LSA_score = similarity(tokenized_texts)
    for score in LSA_score:
        if score == 0.0:
            return

    # add back to topic:
    topic['tokens'] =  ' '.join(tokenized_texts.pop())
    assert len(topic['tokens']) != 0
    logging.info('LSA score: ', LSA_score)
    LSA_score.pop()
    for k, v in topic['language'].items():
        v['tokens'] = ' '.join(tokenized_texts.pop())
        assert len(v['tokens']) != 0
        v['LSA_score'] = LSA_score.pop()
        #TODO: make sure this is a float or integer.
        print(v['LSA_score'])

    return (topic)


def batch_similarity_processing():
    print("This program will process your entire DB for similarity.  If you have done this already, the information will be overwritten. CNTRL-C to cancel.")
    compare = input("LSA or TFIDF? : ").lower()
    if compare not in ['lsa', 'tfidf']:
        sys.exit('Input lsa or tfidf')
    titles = datastore.get_all_titles_from_db()
    for title in titles:
        print('working: ', title)
        tokens_and_langs = datastore.get_edition_topic_tokens(title[0])
        tokens = [token[0].split(' ') for token in tokens_and_langs]
        scores = similarity(tokens, compare)[1:] # get rid of English
        try:
            langs = [lang[1] for lang in tokens_and_langs][1:]
        except IndexError: # can happen if there is only an English entry.
            continue
        for score, lang in zip(scores, langs):
            datastore.store_nlp_to_db(compare, title[0], lang, score)
            print('updated ' + title[0] + ', ' + str(lang))


if __name__ == '__main__':
    batch_similarity_processing()