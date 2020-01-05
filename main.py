#!python3

"""
Something something great program, great programmer, license.
"""
from compare_docs import compare_docs
from datastore import initialize_db, store_topic_to_db
from get_articles import get_topic_articles

from datetime import datetime


def main():
    start = datetime.now()
    initialize_db()
    store_topic_to_db(compare_docs(get_topic_articles()))
    print("Duration to process the topic =", str(datetime.now() - start))


if __name__ == '__main__':
    main()