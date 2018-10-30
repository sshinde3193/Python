import unittest
from Task_4 import file_list

class myTest(unittest.TestCase):

    def test_file_list(self):
        filename = 'test1.txt'
        list = file_list(filename)
        self.assertEqual(3, len(list))                                                      # Case_1: The file used has 3 lines, therefore this checks whether its reading the file which has 3 lines
        self.assertEqual(str(list), 'Yossarian decided\nnot to utter\nanother word.\n')     # Case_2: The case reads the file and checks against hardcoded input of the file, to check if its reading the correct file

if __name__ == '__main__':
    unittest.main()
