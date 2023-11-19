import util

from abc import ABC, abstractmethod
from typing import Optional

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# 추상 클래스 정의
class Plotter(ABC):
    def __init__(self) -> None:
        sns.set()
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 8))       
        plt.rcParams['font.weight'] = 'bold'
        plt.rcParams['axes.labelweight'] = 'bold'
        sns.set_palette("dark")
        #sns.set_context("talk")
        plt.tick_params(labelsize=23)
        return

    @abstractmethod
    def ShowPlot(self, x: str, y: str, data: pd.DataFrame, hue: Optional[str] = None) -> Optional[bool]:
        plt.show()
        return True

    def SetTitle(self, title: str) -> None:
        plt.title(title, fontsize=30, weight='bold')  
        return

    def SetXlabel(self, xlabel: str) -> None:
        plt.xlabel(xlabel=xlabel, fontsize=28, weight='bold')
        return

    def SetYlabel(self, ylabel: str) -> None:
        plt.ylabel(ylabel=ylabel, fontsize=28, weight='bold')
        return


