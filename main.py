#!python3

"""
Something something great program, great programmer, license.
"""
from compare_docs import compare_docs
from datastore import initialize_db, store_topic_to_db
from get_articles import get_articles


def main():
    initialize_db()
    store_topic_to_db(compare_docs(get_articles()))


if __name__ == '__main__':
    main()