import util

import unittest
import pandas as pd
from Plotters.BoxPlotter import BoxPlotter
from Drawers.DataFusion import DataFusion
import unittest
from unittest.mock import patch

class TestBoxPlotter(unittest.TestCase):
    def setUp(self) -> None:
        self.plotter = BoxPlotter()
        return super().setUp()
    
    def test_CallShowPlot(self):
        data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})
        # Mock the super().ShowPlot method
        with patch.object(BoxPlotter, 'ShowPlot') as mock_show_plot:
            # Call the ShowPlot method
            self.plotter.ShowPlot('x', 'y', data)

            # Assert that the super().ShowPlot method was called with the correct arguments
            mock_show_plot.assert_called_with('x', 'y', data)

    
    def test_ShowPlotwithHue(self):
        df = DataFusion()
        
        exResultDataSet = df.GetLoadedData()
        exResultDataSet = exResultDataSet[exResultDataSet["Set Number"] > 110]
        exResultDataSet = exResultDataSet[120 > exResultDataSet["Set Number"]]
                        

        # Call the ShowPlot method
        result = self.plotter.ShowPlot(x = "Set Number", y="Celsius", data = exResultDataSet, hue="Sensor")      

        # Assert that the result is None
        self.assertTrue(result)
