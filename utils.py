#!python

import csv
import os

def read_ASCII_txt_to_string_in_chunks(filename, chunk_size=5000):
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



def write_string_to_txt_file(filename, translated_text):
    with open(filename, 'w+') as f:
        f.write(translated_text)




###############


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