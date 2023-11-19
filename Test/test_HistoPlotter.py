import unittest
import pandas as pd
from unittest.mock import patch
from Plotters.HistoPlotter import HistoPlotter
from Drawers.DataFusion import DataFusion

class TestHistoPlotter(unittest.TestCase):
    def setUp(self):
        self.plotter = HistoPlotter()
        return super().setUp()

    def test_CallShowPlot(self):
        data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})
        
        with patch.object(HistoPlotter, 'ShowPlot') as mock_show_plot:
            self.plotter.ShowPlot('x', 'y', data)
            mock_show_plot.assert_called_with('x', 'y', data)

    def test_ShowPlotwithHue(self):
        df = DataFusion()
        exResultDataSet = df.GetLoadedData()
        result = self.plotter.ShowPlot(x="Celsius", data=exResultDataSet, hue="Sensor")   
        self.assertTrue(result)

        

if __name__ == '__main__':
    unittest.main()

