import unittest
from Task_4 import QuadraticProbeHashTable
from Task_4 import read_file

class myTest(unittest.TestCase):

    def test_hash(self):
        obj = QuadraticProbeHashTable(250727, 1)
        x = obj.hash('test')
        y = obj.hash('test')
        self.assertEqual(x, y)                                      # Case_1: Equal items have equal hash values
        self.assertGreaterEqual(x, 0)
        self.assertLessEqual(x, obj.table_size)                     # Case_2: The hash value is between 0 and table size

    def test_setitem(self):
        obj = QuadraticProbeHashTable(250727, 1)
        obj.__setitem__('test', 'test')
        self.assertEqual(1, obj.count)                          # Case_1: count increments by 1 when object is inserted into the table
        x = obj.__getitem__('test')
        self.assertEqual(x, 'test')                             # Case_2: Checks whether test is inside the hashtable, returns True if so x equals 'test'
        obj1 = QuadraticProbeHashTable(250727, 1)
        obj1.__init__(2, 1)
        obj1.__setitem__('A', 'test1')
        obj1.__setitem__('B', 'test2')
        with self.assertRaises(Exception):                      # Case_3: Raises an exception when the table is full, in this case table is full with size 2
            obj1.__setitem__('D', 'test4')

    def test_getitem(self):
        obj = QuadraticProbeHashTable(250727, 1)
        obj.__setitem__('A', 'test')
        obj.__setitem__('B', 'test1')
        x = obj.__getitem__('A')                        # Case_1: We get the item at the key 'A' i.e. 'test' and we check if the variable we store is equal to the value
        self.assertEqual(x, 'test')
        with self.assertRaises(KeyError):
            obj.__getitem__('C')                           # Case_2: if the key is not found, raises keyerror
        obj1 = QuadraticProbeHashTable(250727, 1)
        obj1.__init__(2, 1)
        obj1.__setitem__('D', 'test3')
        obj1.__setitem__('E', 'test4')
        with self.assertRaises(KeyError):
            obj1.__getitem__('Bazil')                           # Case_3: Raises KeyError if loop exits without returning meaning no key found in hash table

    def test_contains(self):
        obj = QuadraticProbeHashTable(250727, 1)
        obj.__setitem__('A', 'test')
        obj.__setitem__('C', 'test1')
        self.assertTrue(obj.__contains__('A'))                          # Case_1: If the hash table contains the key 'A', it will return True
        self.assertFalse(obj.__contains__('B'))                         # Case_2: If the hash table does not contain 'B', it will return False


    def test_read_file(self):
        filename = 'english_small.txt'
        obj = QuadraticProbeHashTable(250727, 1)
        read_file(filename, obj)
        self.assertEqual(84097, obj.count)                  # Case_1: The file used has 3 lines, therefore this checks whether its reading the file which has 3 lines
        
        
if __name__ == '__main__':
    unittest.main()
