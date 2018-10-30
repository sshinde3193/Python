import unittest
from Task_5 import SeperateChainingHashTable
from Task_5 import read_file


class myTest(unittest.TestCase):

    def test_hash(self):
        obj = SeperateChainingHashTable(250727, 1)
        x = obj.hash('test')
        y = obj.hash('test')
        self.assertEqual(x, y)                                      # Case_1: Equal items have equal hash values
        self.assertGreaterEqual(x, 0)
        self.assertLessEqual(x, obj.table_size)                     # Case_2: The hash value is between 0 and table size

    def test_setitem(self):
        obj = SeperateChainingHashTable(250727, 1)
        obj.__setitem__('test', 'test')
        self.assertEqual(1, obj.count)                          # Case_1: count increments by 1 when object is inserted into the table
        x = obj.__getitem__('test')
        self.assertEqual(x, 'test')                             # Case_2: Checks whether test is inside the hashtable, returns True if so x equals 'test'

    def test_getitem(self):
        obj = SeperateChainingHashTable(250727, 1)
        obj.__setitem__('A', 'test')
        obj.__setitem__('B', 'test1')
        x = obj.__getitem__('A')                        # Case_1: We get the item at the key 'A' i.e. 'test' and we check if the variable we store is equal to the value
        self.assertEqual(x, 'test')
        with self.assertRaises(Exception):
            obj.__getitem__('C')                        # Case_2: if the key entered has an empty position, None is returned

    def test_contains(self):
        obj = SeperateChainingHashTable(250727, 1)
        obj.__setitem__('A', 'test')
        obj.__setitem__('C', 'test1')
        self.assertTrue(obj.__contains__('A'))                  # Case_1: If the hash table contains the key 'A', it will return True
        self.assertFalse(obj.__contains__('B'))                 # Case_2: If the hash table does not contain 'B', it will return False

    def test_read_file(self):
        filename = 'english_small.txt'
        obj = SeperateChainingHashTable(250727, 1)
        read_file(filename, obj)
        self.assertEqual(71770,obj.count)                       # Case_1: The file used has 3 lines, therefore this checks whether its reading the file which has 3 lines

if __name__ == '__main__':
    unittest.main()
