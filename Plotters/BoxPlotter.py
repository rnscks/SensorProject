import util

from Plotters.Plotter import Plotter

from typing import Optional

import pandas as pd
import seaborn as sns


class BoxPlotter(Plotter):
    def __init__(self) -> None:        
        super().__init__()
        self.Flierprops = dict(markerfacecolor='#D1180B', marker='d')
        self.Medianprops = dict(linestyle='-', linewidth=4, color = '#D1180B')
        self.Palette = {"DHT11": "#EE4E2C", "DS18": "#3B41CE"}
        return
        
    def ShowPlot(self, x: str, y: str,data: pd.DataFrame, hue: Optional[str] = None)-> Optional[bool]:           
        sns.boxplot(x=x, y=y, data=data, hue=hue, flierprops=self.Flierprops, medianprops = self.Medianprops, palette=self.Palette)
        return super().ShowPlot(x, y, data)
    
    def SetFlier(self, markerfacecolor:str, marker:str) -> None:
        self.Flierprops = dict(markerfacecolor=markerfacecolor, marker=marker)
        return
    
    def SetMedian(self, linestyle:str, linewidth:int, color:str) -> None:
        self.Medianprops = dict(linestyle=linestyle, linewidth=linewidth, color = color)
        return
    
    def SetPalette(self, hueList:list[str], colors:list[str]) -> None:
        self.Palette = {}

        for i in range(hueList):
            self.Palette[hueList[i]] = colors[i]    
        return  

if (__name__ == "__main__"):
    pass

