import util

from Plotters.Plotter import Plotter

from typing import Optional
from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class HistoPlotter(Plotter):
    def __init__(self) -> None:
        super().__init__()

    def ShowPlot(self, x: str ,data: pd.DataFrame, hue: Optional[str] = None, y:str = "") -> Optional[bool]:           
        sns.histplot(x=x, data=data, hue=hue, multiple="stack", bins=10)
        return super().ShowPlot(x, y, data)