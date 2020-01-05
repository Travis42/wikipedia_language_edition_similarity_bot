#!python3

"""
Something something great program, great programmer, license.
"""
from compare_docs import compare_docs
from datastore import initialize_db, store_topic_to_db
from get_articles import get_topic_articles, move_to_random_topic, move_through_topic
from datetime import datetime
import sys


def main():
    initialize_db()
    visited_topics = ['History']
    topics_to_parse = move_through_topic()
    while topics_to_parse:
        try:
            start = datetime.now()
            page = next(topics_to_parse)
            visited_topics.append(page)
            topic = get_topic_articles(page)
            if not topic:
                continue
            print(topic['title'])
            memory_data_store = compare_docs(topic)
            if not memory_data_store:
                print('Articles have nothing in common, was probably a stub.')
                continue
            store_topic_to_db(memory_data_store)
            print("Duration to process the topic: ", str(datetime.now() - start))
            print()
        except KeyboardInterrupt:
            sys.exit('\nFinished.')


if __name__ == '__main__':
    main()