import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------------------------------')
    print("                  Journal App")
    print('-------------------------------------------------')


def run_event_loop():
    print ('Welcome to your journal. What would you like to do in your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name) # creation of a list!

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it:')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, your entry '{}' isn't valid".format(cmd) )

    print ("Ciao!")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your Journal Entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input("Type your entry. Press <enter> to exit: ") # part of UI
    journal.add_entry(text, data)


main()
