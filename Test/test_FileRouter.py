import unittest
import pandas
from ExprimentResult.FileReader import FileRouter

class TestFileRouter(unittest.TestCase):
    def test_FileRouter(self):
        fr = FileRouter("ExprimentResult")
        result = pandas.read_excel(fr.GetFilePath())
        pass