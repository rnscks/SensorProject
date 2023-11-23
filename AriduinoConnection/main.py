import util

ERROR = -1

def IsError(data1, data2, data3, data4):
    return (data1 == ERROR or data2 == ERROR or data3 == ERROR or data4 == ERROR)

from Paser import Paser
from AriduinoConnection.DataSet import DataSet
from PlotDrawer import PlotDrawer
import pandas as pd
import serial
import time

# MUST MODIFY BEFORE EXPRIMENT!!!! ###########
##############################################
##############################################
ser = serial.Serial('COM3', 9600)           ##
experimentSetNumbering = 20                 ## 
###########################################


dataSet = DataSet(experimentSetNumbering)

while True:
    if ser.in_waiting > 0:
        arduinoStringData = ser.readline().decode().strip()  # 시리얼 데이터 읽기
        
        paser = Paser(arduinoStringData)
        wireSensorName, wireSensorResult, dht11SensorName, dht11SensorResult = paser.Parsing()
        
        if (IsError(wireSensorName, wireSensorResult, dht11SensorName, dht11SensorResult)):
            continue

        if (not (0 <= wireSensorResult <= 100 and 0 <= dht11SensorResult <= 100)):
            continue

        dataSet.DataAppend(wireSensorName, wireSensorResult, dht11SensorName, dht11SensorResult)
        if (dht11SensorResult <= 20):
            break
    time.sleep(0.25) 
    
plotDrawer = PlotDrawer(dataSet)
plotDrawer.LinePlotDraw()

df = pd.DataFrame(dataSet.ExprimentDataSet)
df.to_excel(str(experimentSetNumbering) + "ExprimentReuslt.xlsx")
