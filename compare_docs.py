#!python
from utils import read_txt_to_string, read_txt_to_string_in_chunks, combine_string_generator_pieces

from gensim import corpora, models, similarities
from nltk import word_tokenize
from nltk.corpus import stopwords

from collections import defaultdict, namedtuple
from copy import deepcopy
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


def similarity(documents_list):

    dictionary = corpora.Dictionary(documents_list)
    corpus = [dictionary.doc2bow(text) for text in documents_list]

    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=len(corpus))
    # was len(documents_list)
    vec_lsi = lsi[corpus[0]] # first document is our thing to compare against.

    index = similarities.MatrixSimilarity(lsi[corpus])  # transform corpus to LSI space and index it
    # Options:
    #index.save('/tmp/deerwester.index')
    #index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
    sims = index[vec_lsi]  # perform a similarity query against the corpus
    # format: document #, similarity score

    # return similarities least to most
    #sims = sorted(enumerate(sims), key=lambda x: x[1])
    return list(sims)


def compare_docs(topic):
    # all translations:
    documents = [content['translated_content'] for lang, content in topic['language'].items()]

    # add in English
    documents.insert(0, topic['content'])
    print ('There are this many documents', len(documents))

    # Tokenize
    tokenized_texts = [tokenize(doc) for doc in documents]

    assert len(documents) == len(tokenized_texts)
    # what goes in ^ should come out, same len.
    for tokens in tokenized_texts:
        assert len(tokens) != 0

    # Compare
    LSA_score = similarity(tokenized_texts)
    for score in LSA_score:
        if score == 0.0:
            return

    # add back to topic:
    topic['tokens'] =  ' '.join(tokenized_texts.pop())
    assert len(topic['tokens']) != 0
    print(LSA_score)
    LSA_score.pop()
    for k, v in topic['language'].items():
        v['tokens'] = ' '.join(tokenized_texts.pop())
        assert len(v['tokens']) != 0
        v['LSA_score'] = LSA_score.pop()

    return (topic)