from googletrans import Translator
from utils import read_ASCII_txt_to_string_in_chunks, write_string_to_txt_file

import sys

translator = Translator()

# 2050 chars is the tested sweet spot for Google Translate API, but for some reason it does end up failing eventually.
translated_text = ''
for chunk in read_ASCII_txt_to_string_in_chunks('Glass_Japanese_untranslated.txt', 1500):
    # limit each object to 1000 characters, then stitch back together.
    # this is due to Google Translate's limitation on input size.
    translated_text += translator.translate(chunk).text

write_string_to_txt_file('Glass_Japanese_translated.txt', translated_text)
