import phonebook
import unittest

import pickle
import sys

pb_path = "test_phonebook.pb"

class TestSequenceFunctions(unittest.TestCase):
    # verifies that stdout matches to_match
    def verify(self, to_match):
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("run this script with the -b flag")
        output = sys.stdout.getvalue().strip() 
        self.assertEquals(output, to_match)

    # also tests adding
    def setUp(self):
        pickle.dump({}, open(pb_path, 'wb'))
        phonebook.add(pb_path, "James John", "212 234 2693")
        phonebook.add(pb_path, "John Carter", "212 234 2693")
        phonebook.add(pb_path, "Smith John", "212 234 2693")
        phonebook.add(pb_path, "Wow Doge", "212 234 2693")
        phonebook.add(pb_path, "Sssss Fffff", "917 555 5555")

    def test_add_dup(self):
        phonebook.add(pb_path, "John Carter", "718 298 2959")
        self.verify('"John Carter" already exists in ' + pb_path)

    # exact match
    def test_lookup(self):
        phonebook.lookup(pb_path, "John Carter")
        self.verify('John Carter 212 234 2693')

    # multiple
    def test_lookup_mult(self):
        phonebook.lookup(pb_path, "J")
        self.verify('James John 212 234 2693\nJohn Carter 212 234 2693\nSmith John 212 234 2693')

    # case insensitive
    def test_lookup_lower(self):
        phonebook.lookup(pb_path, "j")
        self.verify('James John 212 234 2693\nJohn Carter 212 234 2693\nSmith John 212 234 2693')

    # partial matching
    def test_lookup_partial(self):
        phonebook.lookup(pb_path, "Doge")
        self.verify('Wow Doge 212 234 2693')

    # failed lookup
    def test_cant_find(self):
        phonebook.lookup(pb_path, "Batman")
        self.verify("")

    # reverse lookup single
    def test_reverse_lookup(self):
        phonebook.reverse_lookup(pb_path, "917 555 5555")
        self.verify('Sssss Fffff 917 555 5555')

    # reverse lookup multiple
    def test_reverse_lookup_mult(self):
        phonebook.reverse_lookup(pb_path, "212 234 2693")
        self.verify('James John 212 234 2693\nJohn Carter 212 234 2693\nSmith John 212 234 2693\nWow Doge 212 234 2693')

    def test_change(self):
        phonebook.change(pb_path, "John Smith", "212")
        phonebook.lookup(pb_path, "John Smith")
        self.verify('John Smith 212')

    def test_change_dne(self):
         phonebook.change(pb_path, "I DNE", "212")
         self.verify("")

if __name__ == '__main__':
    unittest.main()
