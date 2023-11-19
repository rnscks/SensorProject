from DataFusion import DataFusion
from Plotters.LinePlotter import LinePlotter

import numpy as np
import  pandas  as pd


class ErrorRatioData:
    def __init__(self) -> None:
        
        pass
    def GetErrorRatioData(self) -> pd.DataFrame:
        exResultData: pd.DataFrame = DataFusion().GetLoadedData()
        exResultData = exResultData[exResultData["Set Number"] > 30]
        exResultData = exResultData[170 > exResultData["Set Number"]]
        
        ds18_celsius = exResultData[exResultData["Sensor"] == "DS18"]
        dht11_celsius = exResultData[exResultData["Sensor"] == "DHT11"]
        # 'Set Number'를 기준으로 각 DataFrame 정렬
        ds18_celsius_sorted = ds18_celsius.sort_values(by='Set Number')
        dht11_celsius_sorted = dht11_celsius.sort_values(by='Set Number')
        


        # 'Set Number'가 동일한 행끼리 'Celsius' 값을 비교하기 위해 인덱스 리셋
        ds18_celsius_sorted = ds18_celsius_sorted.reset_index(drop=True)
        dht11_celsius_sorted = dht11_celsius_sorted.reset_index(drop=True)

        # DS18과 DHT11 센서 간의 'Celsius' 값 차이 계산
        temperature_difference = dht11_celsius_sorted['Celsius'] - ds18_celsius_sorted['Celsius']
        
        # 차이에 'Set Number' 열 추가
        temperature_difference_df = pd.DataFrame({
            'Set Number': dht11_celsius_sorted['Set Number'],
            'Celsius': temperature_difference
        })
        
        
        ret = temperature_difference_df.groupby('Set Number').mean()
        
        return ret.dropna()

    

if __name__ == "__main__":  
    result = ErrorRatioData().GetErrorRatioData()
    

    lp = LinePlotter()
    lp.SetTitle("Error Ratio Average - Time Step Line Plot")
    lp.SetXlabel("Time Step")  
    lp.SetYlabel("Error Ratio Average") 
    lp.ShowPlot(x = "Set Number", y = "Celsius",data=result, linewidth=2.5)
    