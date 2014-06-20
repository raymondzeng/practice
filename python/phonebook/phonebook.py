#!/usr/bin/python

import sys
import pickle

def new_phonebook(pb_path):
    phonebook = {}
    pickle.dump(phonebook, open(pb_path, 'wb'))
    print 'Created phonebook, ' + pb_path + ' in current directory'

# allows partial lookup, so 'hn' would match with 'John Smith'
# case insensitive
# prints results in alphabetical order, sorted by name
# prints nothing if cant find
def lookup(pb_path, to_lookup):
    try:
        to_lookup = to_lookup.lower()
        phonebook = load(pb_path)

        names = phonebook.keys()
        names.sort()
        for name in names:
            if to_lookup in name.lower():
                print name + ' ' + phonebook[name]
    except:
        print pb_dne(pb_path)

def add(pb_path, name, number):
    try:
        phonebook = load(pb_path)
        if name in phonebook:
            print '"' + name + '"' + ' already exists in ' + pb_path
            return
        phonebook[name] = number
        save(phonebook, pb_path)
    except:
        print pb_dne(pb_path)

def change(pb_path, name, new_number):
    try:
        phonebook = load(pb_path)
        try:
            phonebook[name] = new_number
            save(phonebook, pb_path)
        except:
            print name_dne(pb_path, name)
    except:
        pb_dne(pb_path)

def remove(pb_path, name):
    try:
        phonebook = load(pb_path)
        if name in phonebook:
            del phonebook[name]
            save(phonebook, pb_path)
        else:
            print name_dne(pb_path, name)
    except:
        print pb_dne(pb_path)

def reverse_lookup(pb_path, number):
    try:
        phonebook = load(pb_path)
        names = phonebook.keys()
        names.sort()

        for name in names:
            if phonebook[name] == number:
                print name + ' ' + phonebook[name]
    except:
        print pb_dne(pb_path)

# ----- Helpers -----
def load(file_path):
    return pickle.load(open(file_path, 'rb'))

def save(data, file_path):
    pickle.dump(data, open(file_path, 'wb'))
                             
# error messages
def pb_dne(pb_path):
    return "Can't find phonebook: " + pb_path

def name_dne(pb_path, name):
    return '"' + name + '"' + ' does not exist in ' + pb_path

# ----- Command line args parsing ----

if __name__ == "__main__":
    args = sys.argv
    num_args = len(args)
    
    if num_args < 2:
        print "Not enough arguments."
    else:
        command = args[1]
        
        if command == 'create':
            if num_args != 3:
                print "Usage: create <phonebook_name>"
            else:
                pb_path = args[2]
                new_phonebook(pb_path)
        elif command == 'lookup':
            if num_args != 4:
                print "Usage: lookup <name> <phonebook_name>"
            else:
                to_lookup = args[2]
                pb_path = args[3]
                lookup(pb_path, to_lookup)
        elif command == 'add':
            if num_args != 5:
                print "Usage: add <name> <number> <phonebook_name>"
            else:
                name = args[2]
                number = args[3]
                pb_path = args[4]
                add(pb_path, name, number)
        elif command == 'change':
            if num_args != 5:
                print "Usage: change <name> <new_number> <phonebook_name>"
            else:
                name = args[2]
                new_number = args[3]
                pb_path = args[4]
                change(pb_path, name, new_number)
        elif command == 'remove':
            if num_args != 4:
                print "Usage: remove <name> <phonebook_name>"
            else:
                name = args[2]
                pb_path = args[3]
                remove(pb_path, name)
        elif command == 'reverse-lookup':
            if num_args != 4:
                print "Usage: reverse-lookup <number> <phonebook_name>"
            else:
                number = args[2]
                pb_path = args[3]
                reverse_lookup(pb_path, number)
        else:
            print "Invalid command: " + command
                     
