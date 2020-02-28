#!python3

"""
Something something great program, great programmer, license.
"""
from compare_docs import compare_docs
from datastore import initialize_db, store_topic_to_db
from get_articles import get_topic_articles, move_to_random_topic, move_through_topic
from datetime import datetime
from os import rename
import pickle
import sys
from utils import log_setup, microsoft_char_counter


def main():
    log_setup()
    #rename('wiki-bot.log', 'wiki-bot.log-old')
    initialize_db()
    topics_to_parse = []
    try:
        with open('progress.pickle', 'rb') as f:
            visited_topics = pickle.load(f)
    except:
        visited_topics = ['History']

    topics_to_parse.append(move_through_topic(visited_topics[0]))
    while topics_to_parse:
        try:
            start = datetime.now()
            # Breadth first search:
            try:
                page = next(topics_to_parse[0])
            except StopIteration: 
                topics_to_parse.pop()
                continue
            if 'Category' in page.title():
                topics_to_parse.append(
                    CategorizedPageGenerator(page, recurse=True))
                continue
            # skip what has already been visited:
            if page.title() in visited_topics:
                continue
            # valid page, parse topic:
            topic = get_topic_articles(page)
            if not topic:
                continue
            # valid topic worth comparing:
            visited_topics.append(page.title())

            with open('progress.pickle', 'wb') as f:
                pickle.dump(visited_topics, f)

            print(topic['title'])
            memory_data_store = compare_docs(topic)
            if not memory_data_store:
                continue
            store_topic_to_db(memory_data_store)
            print("Duration to process the topic: ", str(datetime.now() - start))
        except KeyboardInterrupt:
            sys.exit('\nFinished.')


if __name__ == '__main__':
    main()