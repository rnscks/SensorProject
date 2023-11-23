import util


class DataSet:
    def __init__(self, exprimentSetNumbering) -> None:
        self.IndexingNumber = 0
        self.ExprimentSetNumbering = exprimentSetNumbering
        self.ExprimentDataSet = {
            'Index' : [],
            'Set Number' : [],
            'Celsius': [],
            'Sensor': []
        }
        return
    
    def DataAppend(self, wireSensorName, wireSensorResult, dhtSensorName, dhtSensorResult):
        self.IndexingNumber += 1
        self.ExprimentDataSet['Index'].append(self.IndexingNumber)
        self.ExprimentDataSet['Set Number'].append(self.ExprimentSetNumbering)
        self.ExprimentDataSet['Sensor'].append(wireSensorName)
        self.ExprimentDataSet['Celsius'].append(wireSensorResult)
        self.ExprimentDataSet['Index'].append(self.IndexingNumber)
        self.ExprimentDataSet['Set Number'].append(self.ExprimentSetNumbering)
        self.ExprimentDataSet['Sensor'].append(dhtSensorName)
        self.ExprimentDataSet['Celsius'].append(dhtSensorResult)
        return
    