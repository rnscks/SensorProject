import util

from abc import ABC, abstractmethod
from typing import Optional

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# 추상 클래스 정의
class Plotter(ABC):
    def __init__(self) -> None:
        """
        Plotter 클래스의 생성자입니다.
        기본적인 플롯 설정을 초기화합니다.
        """
        sns.set()
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 8))       
        plt.rcParams['font.weight'] = 'bold'
        plt.rcParams['axes.labelweight'] = 'bold'
        sns.set_palette("dark")
        sns.set_context("talk")
        plt.tick_params(labelsize=23)

    @abstractmethod
    def ShowPlot(self, x: str, y: str, data: pd.DataFrame, hue: Optional[str] = None) -> Optional[bool]:
        """
        데이터를 기반으로 Plot을 그리는 메서드입니다.
        
        Parameters:
            data (DataFrame): Plot에 사용할 데이터
        
        Returns:
            None
        """
        plt.show()
        return True

    def SetTitle(self, title: str):
        """
        플롯의 제목을 설정하는 메서드입니다.
        
        Parameters:
            title (str): 플롯의 제목
        
        Returns:
            None
        """
        plt.title(title, fontsize=30, weight='bold')  

    def SetXlabel(self, xlabel: str):
        """
        x축의 레이블을 설정하는 메서드입니다.
        
        Parameters:
            xlabel (str): x축의 레이블
        
        Returns:
            None
        """
        plt.xlabel(xlabel=xlabel, fontsize=28, weight='bold')

    def SetYlabel(self, ylabel: str):
        """
        y축의 레이블을 설정하는 메서드입니다.
        
        Parameters:
            ylabel (str): y축의 레이블
        
        Returns:
            None
        """
        plt.ylabel(ylabel=ylabel, fontsize=28, weight='bold')


