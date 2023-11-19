import util
from Plotters.Plotter import Plotter

from typing import Optional
import pandas as pd
import seaborn as sns


class LinePlotter(Plotter):
    def __init__(self) -> None:
        super().__init__()    

    def ShowPlot(self, x: str, y: str,data: pd.DataFrame, hue: Optional[str] = None) -> Optional[bool]:           
        sns.lineplot(x=x, y=y, data=data, hue=hue)
        return super().ShowPlot(x, y, data)
