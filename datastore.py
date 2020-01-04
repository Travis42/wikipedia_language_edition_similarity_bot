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
    c.execute('''CREATE TABLE primary_articles (
                    id integer not null primary key autoincrement,
                    date text not null,
                    title text not null,
                    content text)''')
    c.execute('''CREATE TABLE translated_articles (
                    id integer not null primary key autoincrement,
                    lang_code text,
                    LSA_score real,
                    orig_title text,
                    orig_content text,
                    translated_content text,
                    foreign key(id) references primary_articles(id))''')
    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


# TODO: this only handles 1 translation.
# see https://docs.python.org/3/library/sqlite3.html for a method to do more.
def store_values_to_db(title, content, lang_code, LSA_score, orig_title, orig_content, translated_content):
    with sqlite3.connect("articles.sqlite") as c:
        # Insert a row of data
        date = datetime.now().strftime("%m/%d/%Y, %H:%M")
        entries = (date, title, content)
        c.execute("INSERT INTO primary_articles(date,title,content) \
                  VALUES (?,?,?)", entries)

        entries = (lang_code, LSA_score, orig_title, orig_content, translated_content)
        c.execute("INSERT INTO translated_articles(\
                  lang_code,LSA_score,orig_title,orig_content,\
                  translated_content) VALUES (?,?,?,?,?)", entries)