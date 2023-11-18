from DataSet import DataSet

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class PlotDrawer:
    def __init__(self, resultDataSet: DataSet) -> None:
        self.ResultDataSet: DataSet = resultDataSet
        pass
    
    def LinePlotDraw(self):

        reusltDataFrame =  pd.DataFrame(self.ResultDataSet.ExprimentDataSet)
        # 그래프 생성
        plt.figure(figsize = (19, 10))
        sns.set_style("whitegrid")

        sns.lineplot(data = reusltDataFrame, x= 'Index', y = 'Celsius', hue= 'Sensor')

        # 그래프 제목과 축 레이블 설정
        plt.title('Temperature Change Graph', fontsize = 30)
        plt.xlabel('Time Step', fontsize = 28)
        plt.ylabel('Celsius', fontsize = 28)
        plt.xticks(fontsize=26)  # x 축 눈금 숫자 크기 조절
        plt.yticks(fontsize=26)  # y 축 눈금 숫자 크기 조절

        plt.legend(title = 'Sensor Type', title_fontsize = 18, fontsize = 18,  loc='upper left', bbox_to_anchor=(1, 0.6))
        exprimentSetNumbering = self.ResultDataSet.ExprimentDataSet['Set Number'][0]
        # 그래프 표시
        plt.savefig(str(exprimentSetNumbering) + "Temperauture Change Graph")
        return