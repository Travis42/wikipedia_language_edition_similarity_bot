#!python


# I'M RIPPING OUT THE GUTS FROM ANOTHER PROJECT.  THIS CODE WONT RUN YET.

from gensim import corpora, models, similarities
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import numpy as np

from API_interface import pull_filenames
from utils import moveToSubfolder

import os
import datetime
import string
import re


def tfidf_process(sentences):
    """
    :param sentences: descriptions of stories
    :return: sims. Each position matches a position in sentences.
    # each value is a numpy ndarray that shows how much other sentences
    # match. The position of each of these corresponds to where they show up
    # in sentences.
    """

    ############### Processing Model
    # STEP 1 : Index and vectorize"

    # create dictionary (index of each element) (creates bag of words count)
    dictionary = corpora.Dictionary(sentences)
    # store the dictionary, for future reference
    # dictionary.save('sentences.dict')

    # compile corpus (vectors number of times each elements appears, bag of
    # words vectors)
    raw_corpus = [dictionary.doc2bow(t) for t in sentences]
    corpora.MmCorpus.serialize('sentences.mm', raw_corpus)  # store to disk

    # STEP 2 : Transform and compute similarity between corpuses"
    # load our dictionary
    dictionary = corpora.Dictionary.load('sentences.dict')

    # load vector corpus
    corpus = corpora.MmCorpus('sentences.mm')

    #########

    # Transform Text with TF-IDF
    tfidf = models.TfidfModel(corpus)  # step 1 -- initialize a model

    # convert our vectors corpus to TF-IDF space
    corpus_tfidf = tfidf[corpus]

    # STEP 3 : Create similarity matrix of all files
    index = similarities.MatrixSimilarity(tfidf[corpus])

    index.save('deerwester.index')
    index = similarities.MatrixSimilarity.load('deerwester.index')

    # get a similarity matrix for all documents in the corpus
    sims = index[corpus_tfidf]

    # print(list(enumerate(sims)))

    # print sorted (document number, similarity score) 2-tuples
    # print(sims[0])
    return sims

# this is where the words are getting tokenized.
def tokenize(df, names, filename):
    x = pd.read_csv(filename, sep=',', encoding='utf8')
    # just get the filename, instead of full path:
    filename = filename.split("/")
    filename = filename[-1][:-4]

    df[filename] = x.loc[:, 'description']
    df['temp'] = x.loc[:, 'description']
    df.temp = df.temp.str.strip().str.lower()
    df.temp = df.temp.astype('str')
    df.temp = df.temp.dropna()
    df.temp = df.temp.str.encode('utf-8').str.decode('ascii', 'ignore')

    # getting rid of punctuation:
    df.temp = df.temp.apply(
        lambda x: re.sub('[' + string.punctuation + ']', '', x))

    # remove English stop words
    stop = stopwords.words('english')
    df.temp = df.temp.apply(
        lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

    # Tokenizing the string w NLTK word_tokenize
    df[filename[:-4] + ' tokenized'] = df.temp.apply(word_tokenize)



def tfidf():
    # create a new DataFrame composed of all tokenized versions:
    tokenized = [col for col in df.columns if 'tokenized' in col]
    X = df.loc[:, tokenized]
    # drop from original so they're distinct:
    not_tokenized = [col for col in df.columns if 'tokenized' not in col]
    df = df.loc[:, not_tokenized]

    # transform to list of lists
    sentences = []
    for col in X.columns:
        for item_no, line in enumerate(X[col].values.tolist()):
            # create sentences to turn into model:
            sentences.append(line)

    # keywords have been extracted and stopwords removed.

    # for sims, each position matches a position in sentences.
    # each value is a numpy ndarray that shows how much other sentences
    # match. The position of each of these corresponds to where they show up
    # in sentences.
    sims = tfidf_process(sentences)





# moving results section
date = datetime.datetime.now().strftime("%m-%d-%Y")
if hits is False:
    os.remove(report + "_results_" + date + ".txt")
else:
    moveToSubfolder('results ' + str(date),
                    report + "_results_" + date + ".txt")
