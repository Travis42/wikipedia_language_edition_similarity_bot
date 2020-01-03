#!python3
"""
SQL schema, stores and retrieves data.

lang_code: language the 'foreign' article is in,
LSA_score: relation to the target/primary language article,
target_lang_content: target/primary lang article, 
orig_content: 'foreign' article content, 
translated_content: 'foreign' article content translated into target language.

TODO: here I see that the db will be language centric in terms of whatever 
language the user is coming from.  Consider adding a config option to 
explicitly state the focus language or mention it in the readme.
"""
import sqlite3

def initialize_db():
connection = sqlite3.connect('articles.sqlite')
c = connection.cursor()
# Create table
c.execute('''CREATE TABLE articles (
                id integer primary key autoincrement,
                date text not null,
                title text not null)''')
c.execute('''CREATE TABLE content (
                id integer not null REFERENCES articles(id),
                lang_code text,
                LSA_score real,
                target_lang_content text,
                orig_content text,
                translated_content text)''')
# Save (commit) the changes
connection.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connection.close()


def store_values_to_db(title, lang_code, LSA_score, target_lang_content, orig_content, translated_content):
    '''
    saves the date accessed, English title, original article, translated article, and LSA scores.
    '''
    connection = sqlite3.connect('articles.sqlite')
    c = connection.cursor()
    # Insert a row of data
    datetime = datetime.now().strftime("%m/%d/%Y, %H:%M")
    entry = f"INSERT INTO articles VALUES ({datetime}, {title})"
    c.execute(entry, params)
    connection.commit()
    entry = f"INSERT INTO articles VALUES ({lang_code}, {LSA_score}, \
                {target_lang_content}, {orig_content}, {translated_content})"
    c.execute(entry, params)
    connection.commit()
    connection.close()