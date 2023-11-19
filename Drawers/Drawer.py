import util
import pandas as pd 
from Plotters.PlotterFactory import PlotterFactory
from DataFusion import DataFusion
from ExprimentResult.FileReader import FileReader   


class Drawer:
    def __init__(self):
        pass

    def DrawHisto(self):
        df = DataFusion()
        exResultDataSet = df.GetLoadedData()   
        
        histoPlotter = PlotterFactory().CreatePlotter("histo")
        histoPlotter.SetTitle("Histogram of Sensor Data")
        histoPlotter.SetXlabel("Celsius")
        histoPlotter.SetYlabel("Frequency")   
        histoPlotter.ShowPlot(x = "Celsius", data = exResultDataSet, hue="Sensor")   

    def DrawBoxPlot(self, right_range:int = 0, left_range:int = 10):
        df = DataFusion()
        exResultDataSet = df.GetLoadedData()   

        exResultDataSet = exResultDataSet[exResultDataSet["Set Number"] > right_range]
        exResultDataSet = exResultDataSet[left_range > exResultDataSet["Set Number"]]
        exResultDataSet['Sensor'] = pd.Categorical(exResultDataSet['Sensor'], categories=['DS18', 'DHT11'], ordered=True)   
        boxPlotter = PlotterFactory().CreatePlotter("box")
        boxPlotter.SetTitle("Box Plot of Temperature Data")
        boxPlotter.SetXlabel("Time Step")
        boxPlotter.SetYlabel("Celsius")
        boxPlotter.ShowPlot(x = "Set Number", y="Celsius", data = exResultDataSet, hue="Sensor")
        


    def DrawLinePlots(self):
        MAX_FILE_NUMBER = 16
        fileReader: FileReader = FileReader()

        for _ in range(MAX_FILE_NUMBER):
            exResultDataSet: pd.DataFrame = fileReader.ReadFile()
            linePlotter = PlotterFactory().CreatePlotter("line")
            linePlotter.SetTitle("Temperature")
            linePlotter.SetXlabel("Time Step")  
            linePlotter.SetYlabel("Celsius")

            linePlotter.ShowPlot(x= "Index", y="Celsius", data=exResultDataSet, hue="Sensor")
            
            





if (__name__ =="__main__"): 
    #Drawer().DrawHisto()
    Drawer().DrawBoxPlot(110, 120)  
    #Drawer().DrawLinePlots()    
    pass