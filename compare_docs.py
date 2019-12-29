#!python
from utils import read_ASCII_txt_to_string_in_chunks,combine_string_generator_pieces

from nltk import word_tokenize
from nltk.corpus import stopwords

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
    return tokenized



# Read
English_doc = combine_string_generator_pieces(read_ASCII_txt_to_string_in_chunks('Glass_English.txt'))
Japananese_tranlated_doc = combine_string_generator_pieces(
    read_ASCII_txt_to_string_in_chunks('Glass_Japanese_translated.txt'))

# TO DO: there might be something to this later
#print(len(tokenize(Japananese_tranlated_doc)))
#print(len(tokenize(English_doc)))

# Tokenize
English_doc = tokenize(English_doc)
Japananese_tranlated_doc = (tokenize(Japanese_tranlated_doc))



