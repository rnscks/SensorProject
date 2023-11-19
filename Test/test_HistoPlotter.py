import unittest
import pandas as pd
from unittest.mock import patch
from Plotters.HistoPlotter import HistoPlotter

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
        x = "x"
        y = "y"
        hue = "category"
        data = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6], "category": ["A", "B", "A"]})
        result = self.plotter.ShowPlot(x = x, y= y, data =data, hue=hue)   
        self.assertTrue(result)

        

if __name__ == '__main__':
    unittest.main()

