import util

from Plotter import Plotter

from typing import Optional
from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class HistoPlotter(Plotter):
    def __init__(self) -> None:
        super().__init__()

    def ShowPlot(self, x: str, y: str,data: pd.DataFrame, hue: Optional[str] = None):           
        sns.histplot(x=x, y=y, data=data, hue=hue)
        return super().ShowPlot(x, y, data)