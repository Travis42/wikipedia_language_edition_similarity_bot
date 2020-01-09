#!python
"""
IO operations, excepting database operations
"""

import csv
from datetime import date, datetime
import logging
import logging.handlers
import os
import pickle
import sys


def log_setup():
    log_handler = logging.handlers.WatchedFileHandler('wiki-bot.log')
    formatter = logging.Formatter(
        '%(asctime)s [%(process)d]: %(message)s',
        '%b %d %H:%M:%S')
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)


def chunkstring(string, length=5000):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def read_txt_to_string_in_chunks(filename, chunk_size=5000):
    with open(filename, 'r') as f:
        # get to the starting marker:
        for piece in read_in_chunks(f, chunk_size):
            # this works
            yield piece


def read_in_chunks(file_object, chunk_size=5000):
    buffer = 0
    while True:
        data = file_object.read(chunk_size)
        # avoid infinite loop?
        if not data:
            break
        yield data


def combine_string_generator_pieces(generator_function):
    '''
    runs through a string generator function and combines its results
    Optionally takes a change fn to modify the string.
    '''
    return ''.join([chunk for chunk in generator_function])


def read_txt_to_string(filename):
    with open(filename, 'r') as f:
        return f.read()


def write_string_to_txt_file(filename, text, write_or_append='a'):
    action = ''
    if write_or_append == 'write':
        action = 'w+'
    with open(filename, action) as f:
        f.write(text)
        f.write('\n')




###############

def microsoft_char_counter():
    """
    keeps a record of how many characters have been used this month.  If the API key is nearing its limits for that month, will shut down the program and let you know.
    """
    try:
        with open('MS-char-count.pickle', 'rb') as f:
            ms_chars, timestart = int(pickle.load(f))
    except IOError as ioerr:
        with open('MS-char-count.pickle', 'wb') as f:
            pickle.dump('0', date.today())
            microsoft_char_counter()
    # check how much time has elapsed:
    now = date.today()
    if ms_chars >= 2000000:
        sys.exit("Quota exceeded for the month!")
    elif (now - timestart) >= datetime.duration(days=28) and ms_chars >= 1950000:
        sys.exit("Quota for the month is near.  Lay off for now.")
    else:
        return ms_chars


def microsoft_char_counter_reset():
    with open('MS-char-count.pickle', 'rb') as f:
        ms_chars, timestart = int(pickle.load(f))
    if datetime.datetime.today - timestart >= datetime.duration(days=30):
        with open('MS-char-count.pickle', 'wb') as f:
            pickle.dump('0', date.today())



################

def moveToSubfolder(foldername, filename):
    # Move it to the /stories dir
    subdir = foldername
    try:
        os.mkdir(subdir)
    except Exception:
        pass

    cwd = os.getcwd()
    # move the file
    os.rename(cwd + '/' + str(filename),
              cwd + '/' + subdir + '/' + str(filename))


def pull_filenames(full_path=True):
    files = []
    # just pull files from this current directory
    for folderName, subfolders, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.endswith('.csv'):
                if full_path == True:
                    files.append(folderName + '/' + filename)
                else:
                    files.append(filename)

        if 'venv' in folderName or '.git' in folderName:
            continue
    return files

def write_to_csv(name, json_file, append=False):
    categories = ["created_at", "current_state", "description", "estimate",
                  "id", "kind", "labels", "name", "owner_ids", "project_id",
                  "requested_by_id", "story_type", "updated_at", "url"]

    current = os.getcwd()
    os.chdir(current + '/stories')
    csvname = str(name)+".csv"
    if append == True:
        f = csv.writer(open(csvname, "a"))
    else:
        f = csv.writer(open(csvname, "w+"))
        # Write CSV Header, If you dont need that, remove this line
        f.writerow(categories)


    for i in json_file:
        # filling in missing data if a category is missing:
        for x in categories:
            try:
                a = i[x]
            except KeyError:
                i[x] = ""

        f.writerow([i["created_at"],
                    i["current_state"],
                    i["description"],
                    i["estimate"],
                    i["id"],
                    i["kind"],
                    i["labels"],
                    i["name"],
                    i["owner_ids"],
                    i["project_id"],
                    i["requested_by_id"],
                    i["story_type"],
                    i["updated_at"],
                    i["url"]
                    ])

    os.chdir(current)
    print('Wrote {} to disk.'.format(name))


if __name__ == '__main__':
    main()