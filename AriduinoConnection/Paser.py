import util

class Paser:
    def __init__(self, sensorResult: str) -> None:
        self.SensorResult: str = sensorResult
        pass
    
    def Parsing(self):
        dataStringList: list[str] = self.SensorResult.split('|')
        print(dataStringList)
        if (len(dataStringList) != 4):
            return -1, -1, -1, -1
        try:
            wireSensorResult = float(dataStringList[1])
            dht11SensorResult = float(dataStringList[3])
        except ValueError:
            return -1, -1, -1, -1
        
        
        return dataStringList[0], wireSensorResult, dataStringList[2], dht11SensorResult
        
if (__name__ == "__main__"):
    pas = Paser("DS18|26.44|DHT11|25.00")
    print(pas.Parsing())