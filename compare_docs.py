#!python
from utils import read_ASCII_txt_to_string_in_chunks,combine_string_generator_pieces

from gensim import corpora, models, similarities
from nltk import word_tokenize
from nltk.corpus import stopwords

from collections import defaultdict
from copy import deepcopy
import re
import string
import sys

# this is where the words are getting tokenized.
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

    return tokenized


def similarity(documents_list):

    dictionary = corpora.Dictionary(documents_list)
    corpus = [dictionary.doc2bow(text) for text in documents_list]

    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    vec_lsi = lsi[corpus[0]] # first document is our thing to compare against.




    index = similarities.MatrixSimilarity(lsi[corpus])  # transform corpus to LSI space and index it
    # Options:
    #index.save('/tmp/deerwester.index')
    #index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
    sims = index[vec_lsi]  # perform a similarity query against the corpus
    print(list(enumerate(sims)))  # print (document_number, document_similarity) 2-tuples
    # format: document #, similarity score



    '''
    ############### Processing Model
    # STEP 1 : Index and vectorize"

    # create dictionary (index of each element) (creates bag of words count)
    dictionary = corpora.Dictionary(documents_list)
    # store the dictionary, for future reference
    dictionary.save('documents_list.dict')

    # compile corpus (vectors number of times each elements appears, bag of
    # words vectors)
    raw_corpus = [dictionary.doc2bow(t) for t in documents_list]
    corpora.MmCorpus.serialize('documents_list.mm', raw_corpus)  # store to disk

    # STEP 2 : Transform and compute similarity between corpuses"
    # load our dictionary
    dictionary = corpora.Dictionary.load('documents_list.dict')

    # load vector corpus
    corpus = corpora.MmCorpus('documents_list.mm')

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
    '''







# Read
English_doc = combine_string_generator_pieces(read_ASCII_txt_to_string_in_chunks('Glass_English.txt'))
Japanese_translated_doc = combine_string_generator_pieces(
    read_ASCII_txt_to_string_in_chunks('Glass_Japanese_translated.txt'))

# TO DO: there might be something to this later
#print(len(tokenize(Japananese_tranlated_doc)))
#print(len(tokenize(English_doc)))

# Tokenize
documents = [English_doc, Japanese_translated_doc]
tokenized_texts = [tokenize(doc) for doc in documents]

# Compare, using TF-IDF
similarity_score = similarity(tokenized_texts)
print(similarity_score)

