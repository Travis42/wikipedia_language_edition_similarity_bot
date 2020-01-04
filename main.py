#!python3

"""
Something something great program, great programmer, license.
"""
from compare_docs import compare_docs
from datastore import initialize_db, store_topic_to_db

def main():
    initialize_db()
    topic = compare_docs()
    store_topic_to_db(topic)


if __name__ == '__main__':
    main()