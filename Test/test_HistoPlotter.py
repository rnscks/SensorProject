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
        # Create a sample dataframe
        data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})
        # Mock the super().ShowPlot method
        with patch.object(HistoPlotter, 'ShowPlot') as mock_show_plot:
            # Call the ShowPlot method
            self.plotter.ShowPlot('x', 'y', data)

            # Assert that the super().ShowPlot method was called with the correct arguments
            mock_show_plot.assert_called_with('x', 'y', data)

    def test_ShowPlotwithHue(self):
        df = DataFusion()
        df.DataLoad()
        result = self.plotter.ShowPlot(x="Celsius", data=df.ExResultDataSet, hue="Sensor")   
        self.assertTrue(result)

        

if __name__ == '__main__':
    unittest.main()

