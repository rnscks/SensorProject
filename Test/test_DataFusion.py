import unittest
from DataFusion import DataFusion


class TestDataFusion(unittest.TestCase):
    """
    This class contains unit tests for the DataFusion class.
    """
    def test_data_load(self):
        """
        Test the DataLoad method of the DataFusion class.
        """
        # create an instance of DataFusion
        df = DataFusion()
        
        # call the DataLoad method
        df.DataLoad()
        
        # check that the resulting dataset is not empty
        self.assertFalse(df.ExResultDataSet.empty)
        
        df.ExResultDataSet.to_excel("test.xlsx")

