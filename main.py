#!python3

"""
Something something great program, great programmer, license.
"""
from compare_docs import compare_docs
from datastore import initialize_db, store_values_to_db

def main():
    initialize_db()
    title, content, lang_code, LSA_score, orig_title, orig_content, translated_content = compare_docs()
    store_values_to_db(title, content, lang_code, LSA_score, orig_title, orig_content, translated_content)



if __name__ == '__main__':
    main()