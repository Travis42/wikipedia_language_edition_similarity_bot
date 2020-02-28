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

import compare_docs

from datetime import datetime
import os
import sqlite3
import sys

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
    connection.commit()
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

#TODO: I can't figure it out, but the LSA score gets garbled when placed by this method.  I have to use the batch processor to get good results.
def store_topic_to_db(topic):
    title, content, pri_tokens, translation_values = parse_topic_dict(topic)
    with sqlite3.connect("articles.sqlite") as c:
        date = datetime.now().strftime("%m/%d/%Y, %H:%M")
        entries = (date, title, content, pri_tokens)
        c.execute("INSERT INTO primary_topics(date,title,content,tokens) \
                  VALUES (?,?,?,?)", entries)

        c.executemany("INSERT INTO translated_topics(\
                  title,lang_code,LSA_score,orig_title,orig_content,translated_content,tokens) VALUES (?,?,?,?,?,?,?)", translation_values)


def get_entries_by_title(title):
    '''
    returns a dict of all items in the db based on the title
    Dict conforms to the format that it was in when it went into the db
    '''
    with sqlite3.connect("articles.sqlite") as c:
        primary = c.execute('''SELECT * from primary_topics where title=(?)''', (title,))
        secondaries = c.execute('''SELECT * from translated_topics where title=(?)''', (title,))

    primary = primary.fetchall()[0]
    entry_dict = {
                  'title' : primary[2],
                  'content' : primary[3],
                  'pri_tokens' : primary[4],
                  'language' : {},
    }

    secondaries = secondaries.fetchall()
    for entry in secondaries:
        lang_code = entry[2]
        entry_dict['language'][lang_code] = {
                    'LSA_score' : entry[3],
                    'title' : entry[4],
                    'orig_content' : entry[5],
                    'translated_content' : entry[6],
                    'tokens': entry[7],
                     }

    return entry_dict


def get_all_titles_from_db():
    with sqlite3.connect("articles.sqlite") as c:
        titles = c.execute('''SELECT title from primary_topics''')
        title_list_of_tuples = titles.fetchall()
    return title_list_of_tuples


def get_primary_topics_count():
    with sqlite3.connect("articles.sqlite") as c:
        rows = c.execute('''SELECT count(*) from primary_topics''')
    return rows.fetchone()[0]


def get_edition_topic_tokens(title):
    '''
    returns list of (lang code, tokens) tuples
    '''
    title = str(title)
    connection = sqlite3.connect('articles.sqlite')
    c = connection.cursor()
    en_tokens = c.execute('''SELECT tokens from primary_topics where title=(?)''', (title,))
    tokens = en_tokens.fetchall()
    tokens[0] += 'en',
    forn_tokens = c.execute('''SELECT tokens, lang_code from translated_topics where title=(?)''', (title,))
    forn_tokens = forn_tokens.fetchall()
    forn_tokens = [item for item in forn_tokens if item[0] is not None]

    #integrity check
    for token, lang in forn_tokens:
        if len(token) == 0:
            # TODO: fix.  I have areas of the db that are still 'blobs'.  and now its a silent error.
            try:
                content = c.execute('''SELECT translated_content from translated_topics where title=(?) and lang_code=(?)''', (title, lang)).fetchall()[0][0]
            except:
                content = c.execute('''SELECT translated_content from translated_topics where title=(?) and lang_code=(?)''', (title, lang)).fetchall()
                print('something is wrong.  Here is the content of the db: ')
                print(content, token, title, lang)
                sys.exit()
            token = ' '.join(compare_docs.tokenize(content))
            c.execute('''UPDATE translated_topics set tokens=? where title=? and lang_code=?;''',(token, title, lang))
            token = c.execute('''SELECT tokens from translated_topics where title=(?) and lang_code=(?)''', (title, lang)).fetchall()[0][0]
            if not token:
                c.execute('''delete from translated_topics where title=(?) and lang_code=(?)''', (title, lang))
            connection.commit()
            get_edition_topic_tokens(title)

    tokens.extend(forn_tokens)
    connection.commit()
    connection.close()
    return tokens


def store_nlp_to_db(process, title, lang, score):
    with sqlite3.connect("articles.sqlite") as c:
        if process == 'lsa':
            c.execute('''UPDATE translated_topics set LSA_score=? where title=? and lang_code=?;''',(str(score), title, lang))
        elif process == 'tfidf':
            c.execute('''UPDATE translated_topics set tfidf_score=? where title=? and lang_code=?;''',(str(score), title, lang))
