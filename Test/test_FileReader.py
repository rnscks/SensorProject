import unittest
from FileReader import FileReader



class TestFileReader(unittest.TestCase):
    def test_FileRearder(self):
        fr = FileReader()
        for i in range(0, 16):
            result = fr.ReadFile()

            
        pass