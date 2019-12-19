import os

def load(name):
    """
    This method creates and loads a new journal entry

    :param name: this base name of the journal to load
    :return: A new journal data structure populated with the file data
    """
    data = []
    file_name = get_path(name)
    if os.path.exists(file_name):
        with open(file_name) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(name, journal_data):
    file_name = get_path(name)
    print(".....saving to {}".format(file_name))

    with open(file_name, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n') # allows entries to be on separate lines


def get_path(name):
    file_name = os.path.abspath(os.path.join('.', 'journals/', name + '.jrl'))
    return file_name


def add_entry(text, journal_data):
    journal_data.append(text)