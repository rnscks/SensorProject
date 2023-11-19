import util
import pandas as pd
from FileReader import FileReader    
from Plotters.HistoPlotter import HistoPlotter


# max file number is 16 
MAX_FILE_NUMBER = 16
import pandas as pd
from DataFilter import DataFilter

class DataFusion:
    def __init__(self) -> None:
        self.ExResultDataSet: pd.DataFrame = pd.DataFrame()
        self._FileReader: FileReader = FileReader()
        pass
    
    def DataLoad(self) -> None:
        for _ in range(MAX_FILE_NUMBER):
            fileExReusltDataset = self._FileReader.ReadFile()
            fileExReusltDataset = DataFilter(fileExReusltDataset).Filtering()
            self.ExResultDataSet = pd.concat([fileExReusltDataset, self.ExResultDataSet])
            
            
                
if (__name__ =="__main__"):
    df = DataFusion()
    df.DataLoad()
    hp =  HistoPlotter()    
    
    hp.SetTitel("Histogram")
    hp.SetXlabel(xlabel="Celsius")
    hp.SetYlabel(ylabel="Frequency")

    hp.ShowPlot(x = "Celsius", data = df.ExResultDataSet, hue="Sensor")   
