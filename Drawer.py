from Plotters.PlotterFactory import PlotterFactory
from DataFusion import DataFusion

class Drawer:
    def __init__(self):
        pass

    def DrawHisto(self):
        df = DataFusion()
        df.DataLoad()   
        histoPlotter = PlotterFactory().CreatePlotter("histo")
        histoPlotter.SetTitle("Histogram of Sensor Data")
        histoPlotter.SetXlabel("Celsius")
        histoPlotter.SetYlabel("Frequency")   
        histoPlotter.ShowPlot(x = "Celsius", data = df.ExResultDataSet, hue="Sensor")   

    def DrawBoxPlot(self, right_range:int = 0, left_range:int = 10):
        df = DataFusion()
        df.DataLoad()
        df.ExResultDataSet = df.ExResultDataSet[df.ExResultDataSet["Set Number"] > right_range]
        df.ExResultDataSet = df.ExResultDataSet[left_range > df.ExResultDataSet["Set Number"]]
        boxPlotter = PlotterFactory().CreatePlotter("box")
        boxPlotter.SetTitle("Box Plot of Sensor Data")
        boxPlotter.SetXlabel("Time Step")
        boxPlotter.SetYlabel("Celsius")
        boxPlotter.ShowPlot(x = "Set Number", y="Celsius", data = df.ExResultDataSet, hue="Sensor")



if (__name__ =="__main__"): 
    #Drawer().DrawHisto()
    #Drawer().DrawBoxPlot(110, 120)  
    pass