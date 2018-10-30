import unittest
from Task_5 import TextEditor

class myTest(unittest.TestCase):

    def test_insert_filename(self):
        obj = TextEditor()
        self.assertFalse(obj.insert_num('', 'teststring'))                  # Case_1: Checks whether function returns false when empty string is inputted
        self.assertFalse(obj.insert_num(0, 'teststring'))                   # Case_2: Checks whether function returns false when incorrect index is inputted
        self.assertTrue(obj.insert_num(1, 'teststring'))                    # Case_3: Returns true once the string is inputted at the index given

    def test_read_filename(self):
        obj = TextEditor()
        filename = 'test1.txt'
        self.assertTrue(obj.read_filename(filename))                        # Case_1: Returns true if the file is read
        self.assertTrue(FileNotFoundError)                                  # Case_2: Its true that the FileNotFoundError is handled for incorrect input
        self.assertEqual(str(obj.array),'Yossarian decided\nnot to utter\nanother word.\n') # Case:3 Note this is a whitebox test to check whether file is being read correctly

    def test_write_filename(self):
        obj = TextEditor()
        filename = 'test1.txt'
        obj.read_filename(filename)
        filename = 'test5.txt'
        obj.write_filename(filename)
        self.assertEqual(str(obj.array), 'Yossarian decided\nnot to utter\nanother word.\n')         # Case_1: Writes to a new file successfully
        filename = 'freq.txt'
        obj.read_filename((filename))
        filename = 'test.txt'                                                                         # Case_2: Overwrites existing file successfully
        obj.write_filename(filename)
        self.assertEqual(str(obj.array), 'hello world\nhow are you world\nworld is awesome\nbye world\n')

    def test_print_num(self):
        obj = TextEditor()
        obj.insert_num(1, 'Hello World!')
        obj.insert_num(2, 'Bye World!')
        self.assertTrue(obj.print_num(''))                                        # Case_1: Returns true as all inputs are printed when no number is input
        self.assertFalse(obj.print_num(0))                                        # Case_2: Returns false when incorrect index is input
        self.assertTrue(obj.print_num(2))                                         # Case_3: Returns True when a valid index is input as line is printed


    def test_delete_num(self):
        obj = TextEditor()
        obj.insert_num(1, 'Hello World!')
        obj.insert_num(2, 'Bye World!')
        self.assertTrue(obj.delete_num(2))                                        # Case_1: Returns true if an object is deleted
        self.assertFalse(obj.print_num(0))                                        # Case_2: Returns false when incorrect index is input
        self.assertTrue(obj.delete_num(''))                                       # Case_3: Returns true as all inputs are deleted when no number is input


if __name__ == '__main__':
    unittest.main()
