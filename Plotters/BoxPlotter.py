import util

from Plotters.Plotter import Plotter

from typing import Optional

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class BoxPlotter(Plotter):
    def __init__(self) -> None:        
        super().__init__()
        
    def ShowPlot(self, x: str, y: str,data: pd.DataFrame, hue: Optional[str] = None)-> Optional[bool]:           
        sns.boxplot(x=x, y=y, data=data, hue=hue)
        return super().ShowPlot(x, y, data)

if (__name__ == "__main__"):
    pass

