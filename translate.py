from googletrans import Translator
from utils import read_ASCII_txt_to_string_in_chunks, write_string_to_txt_file

import sys

translator = Translator()

translated_text = ''
for piece in read_ASCII_txt_to_string_in_chunks('Glass_Japanese_untranslated.txt', 1000):
    # limit each object to 1000 characters, then stitch back together.
    # this is due to Google Translate's limitation on input size.
    translated_text += translator.translate(piece).text
    

write_string_to_txt_file('Glass_Japanese_translated.txt', translated_text)

