#!python3
"""
SQL schema, stores and retrieves data.

title: 'primary' lang articel title,
content: 'primary' lang article content,
lang_code: language the 'foreign' article is in,
LSA_score: relation to the target/primary language article,
target_lang_content: target/primary lang article, 
orig_title: title entry in original language,
orig_content: 'foreign' article content, 
translated_content: 'foreign' article content translated into target language.

TODO: here I see that the db will be language centric in terms of whatever 
language the user is coming from.  Consider adding a config option to 
explicitly state the focus language or mention it in the readme.
"""
from datetime import datetime
import os
import sqlite3

def initialize_db():
    if os.path.isfile('articles.sqlite'):
        return
    connection = sqlite3.connect('articles.sqlite')
    c = connection.cursor()
    # Create table
    c.execute('''PRAGMA foreign_keys = ON;''')
    c.execute('''CREATE TABLE primary_topics (
                    id integer not null primary key autoincrement,
                    date text not null,
                    title text not null,
                    content text,
                    tokens text)''')
    c.execute('''CREATE TABLE translated_topics (
                    id integer not null primary key autoincrement,
                    title text,
                    lang_code text,
                    LSA_score real,
                    orig_title text,
                    orig_content text,
                    translated_content text,
                    tokens text,
                    foreign key(title) references primary_topics(title))''')
    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def parse_topic_dict(topic):
    # primary lang
    title = topic['title']
    content = topic['content']
    pri_tokens = topic['tokens']

    # translations
    translation_values = []
    for k, v in topic['language'].items():
        lang_code = k
        LSA_score = v['LSA_score']
        orig_title = v['title']
        orig_content = v['orig_content']
        translated_content = v['translated_content']
        tokens = v['tokens']
        translation_values.append((title, lang_code, LSA_score, orig_title, \
                                  orig_content, translated_content, tokens))
    return (title, content, pri_tokens, translation_values)


def store_topic_to_db(topic):
    title, content, pri_tokens, translation_values = parse_topic_dict(topic)

    with sqlite3.connect("articles.sqlite") as c:
        date = datetime.now().strftime("%m/%d/%Y, %H:%M")
        entries = (date, title, content, pri_tokens)
        c.execute("INSERT INTO primary_topics(date,title,content,tokens) \
                  VALUES (?,?,?,?)", entries)

        c.executemany("INSERT INTO translated_topics(\
                  title,lang_code,LSA_score,orig_title,orig_content,translated_content,tokens) VALUES (?,?,?,?,?,?,?)", translation_values)


#def check_topic_in_db()
