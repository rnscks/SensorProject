import pandas as pd
from FileReader import FileReader


# max file number is 16 
MAX_FILE_NUMBER = 16
import pandas as pd
from FileReader import FileReader
from DataFilter import DataFilter

class DataFusion:
    """
    A class for fusing data from multiple files into a single dataset.

    Attributes:
        ExResultDataSet (pd.DataFrame): The resulting dataset after fusing all the data.
        _FileReader (FileReader): An instance of the FileReader class used to read data from files.

    Methods:
        DataLoad(): Loads data from files and concatenates them to the existing dataset.
    """

    def __init__(self) -> None:
        self.ExResultDataSet: pd.DataFrame = pd.DataFrame()
        self._FileReader: FileReader = FileReader()
        pass
    
    def DataLoad(self) -> None:
        """
        Load data from files and concatenate them to the existing dataset.

        Parameters:
            None

        Returns:
            None
        """
        for _ in range(MAX_FILE_NUMBER):
            fileExReusltDataset = self._FileReader.ReadFile()
            fileExReusltDataset = DataFilter(fileExReusltDataset).Filtering()
            self.ExResultDataSet = pd.concat([fileExReusltDataset, self.ExResultDataSet])
            
            
                
            
