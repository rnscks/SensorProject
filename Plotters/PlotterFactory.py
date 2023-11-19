import util
from Plotters.BoxPlotter import BoxPlotter
from Plotters.LinePlotter import LinePlotter
from Plotters.HistoPlotter import HistoPlotter

class PlotterFactory:
    def CreatePlotter(self, plotterType):
        if plotterType == "box":
            return BoxPlotter()
        elif plotterType == "line":
            return  LinePlotter()
        elif plotterType == "histo":
            return HistoPlotter()
        else:
            raise ValueError("Unknown plotter type")
        
if __name__ == "__main__":  
    pass