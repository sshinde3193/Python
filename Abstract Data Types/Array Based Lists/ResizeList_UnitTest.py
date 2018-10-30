import unittest
from Task_2 import ArrayOperations

class myTest(unittest.TestCase):

    def test_str(self):
        obj = ArrayOperations()
        self.assertEqual(str(obj), "")                                   # Case_1: checks whether the empty list gives ""
        obj.append(1)
        obj.append(2)
        self.assertEqual(str(obj), "1\n2\n")                             # Case_2: For the list [1,2], we will get "1\n2\n"

    def test_len(self):
        obj = ArrayOperations()
        self.assertEqual(0, len(obj))                                    # Case_1: Checks whether the self.count = 0
        obj.append(1)
        obj.append(2)
        self.assertEqual(2, len(obj))                                    # Case_2: Appends two items into list to check whether self.count = 2

    def test_contains(self):
        obj = ArrayOperations()
        obj.append(1)
        obj.append(2)
        self.assertTrue(obj.__contains__(1))                             # Case_1: list contains 1, hence will give us true
        self.assertFalse(obj.__contains__(4))                            # Case_2: list does not contain 4 hence will give false

    def test_getitem(self):
        obj = ArrayOperations()
        obj.append(20)
        obj.append(40)
        with self.assertRaises(IndexError):
            obj.__getitem__(2)                                           # Case_1: Index 2 is out of range since count is 2, only index 0 and 1 exist, hence indexerror will be raised
        self.assertLess(1, len(obj))                                     # Case_2: Index 1 is in range, as two items apppended to give self.count = 2 (index < count i.e. index in range)
        with self.assertRaises(IndexError):
            obj.__getitem__(-1)                                          # Case_3: Accounting for negative indexes which are also out of range

    def test_setitem(self):
        obj = ArrayOperations()
        with self.assertRaises(IndexError):
            obj.__setitem__(5, 20)                                       # Case_1: Index 5 is out of range hence indexerror will be raised
        obj.append(1)
        obj.append(2)
        self.assertLess(1, len(obj))                                     # Case_2: Index 1 is in range, as two items apppended to give self.count = 2 (index < count i.e. index in range)
        with self.assertRaises(IndexError):
            obj.__setitem__(-4, 20)                                      # Case_3: Accounting for negative indexes which are also out of range

    def test_eq(self):
        obj = ArrayOperations()
        other = [1,2,3,4]
        obj.append(2)
        obj.append(3)
        self.assertFalse(obj.__eq__(other))                              # Case_1: If the length of the original list is not equal to the length of the other list, then assertFalse
        other1 = [2,3,5,6]
        obj.append(5)
        obj.append(6)
        self.assertTrue(obj.__eq__(other1))                              # Case_2: Checks whether every index of both the lists is the same, if so, assertTrue

    def test_append(self):
        obj = ArrayOperations()
        obj.append(20)
        obj.append(40)
        self.assertEqual(40, obj[1])                           # Case_1: Checks whether the item appended is at the last index, if last appended item equals index count - 1, its true
        self.assertLess(0, len(obj))                          # Case_2: Checks whether the initial count = 0 is less than the new count after appending items into the list
        self.assertEqual(2, len(obj))                         # Case_3: Checks whether after appending 2 items, count = 2


    def test_insert(self):
        obj = ArrayOperations()
        obj.append(1)
        obj.append(2)
        obj.append(3)
        obj.insert(2,4)                                            # Case_1: Inserts item 4 at index 2 and shifts 3 to the right, checks whether this occurs, if so test passes
        self.assertEqual([1,2,4,3], obj)
        with self.assertRaises(IndexError):                        # Case_2: Checks whether it raises indexerror for an index > len(obj)
            obj.insert(5, 20)

    def test_delete(self):
        obj = ArrayOperations()
        obj.append(30)
        obj.append(40)
        obj.append(50)                                                    # obj count initially 3
        obj.delete(1)                                                     # after delete obj count 2
        self.assertEqual(2, len(obj))                                     # Case_1: checks whether the delete function works by comparing whether the count is equal to length after deleting an item at index 1
        self.assertEqual(50, obj.__getitem__(1))                          # Case_2: Checks whether the list has shifted after deletion of an item, this test proves that 50 has moved to index 1 from index 2
        with self.assertRaises(IndexError):
            obj.delete(3)                                                 # Case_3: Checks whether the index is less than the count to check if index is valid

    def test_remove(self):
        obj = ArrayOperations()
        obj.append(30)
        obj.append(40)
        obj.append(50)
        obj.remove(40)
        self.assertEqual(2, len(obj))                                   # Case_1: checks whether the delete function works by comparing whether the count is equal to length after deleting an item at index 1
        self.assertEqual(50, obj.__getitem__(1))                        # Case_2: Checks whether the list has shifted after deletion of an item, this test proves that 50 has moved to index 1 from index 2
        with self.assertRaises(ValueError):                             # Case_3: Since 6 does not exist as an item in the list, the ValueError is raised.
            obj.remove(6)

    def test_resize_list(self):
        obj = ArrayOperations()
        obj.append(150)
        obj.append(175)
        self.assertEqual(100, len(obj.array))                           # Case_1: checks for the if condition failing, when the list is not full, the size remains the same i.e. 100
        for i in range(len(obj.array)):                                 # Case_2: appends items into the list equal to the len of the array, to check that when the array is full, if it resizes the array by 10 times to a len of 1000
            obj.append(i)
        self.assertEqual(1000, len(obj.array))
        self.assertIn(150, obj.array)                                   # Case_3: To check whether the original elements in the list are copied back into it after re-sizing
        self.assertIn(175, obj.array)


if __name__ == '__main__':
    unittest.main()
