import util
import pandas as pd
from ExprimentResult.FileReader import FileReader    
from Plotters.HistoPlotter import HistoPlotter


# max file number is 16 
MAX_FILE_NUMBER = 16
import pandas as pd
from DataFilter import DataFilter

class DataFusion:
    def __init__(self) -> None:

        pass
    
    def GetLoadedData(self) -> None:
        exResultDataSet: pd.DataFrame = pd.DataFrame()
        fileReader: FileReader = FileReader()
        
        for _ in range(MAX_FILE_NUMBER):
            fileExReusltDataset = fileReader.ReadFile()
            fileExReusltDataset = DataFilter(fileExReusltDataset).Filtering()
            exResultDataSet = pd.concat([fileExReusltDataset, exResultDataSet])
        return exResultDataSet
            
            
                
if (__name__ =="__main__"):
    df = DataFusion()
    loadedDataFrame = df.GetLoadedData()
    hp =  HistoPlotter()    
    
    hp.SetTitel("Histogram")
    hp.SetXlabel(xlabel="Celsius")
    hp.SetYlabel(ylabel="Frequency")

    hp.ShowPlot(x = "Celsius", data = loadedDataFrame, hue="Sensor")   
