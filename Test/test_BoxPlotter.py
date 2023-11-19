import unittest
import pandas as pd
from Plotters.BoxPlotter import BoxPlotter
import unittest
from unittest.mock import patch

class TestBoxPlotter(unittest.TestCase):
    def setUp(self) -> None:
        self.plotter = BoxPlotter()
        return super().setUp()
    
    def test_CallShowPlot(self):
        # Create a sample dataframe
        data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})
        # Mock the super().ShowPlot method
        with patch.object(BoxPlotter, 'ShowPlot') as mock_show_plot:
            # Call the ShowPlot method
            self.plotter.ShowPlot('x', 'y', data)

            # Assert that the super().ShowPlot method was called with the correct arguments
            mock_show_plot.assert_called_with('x', 'y', data)

    
    def test_ShowPlot(self):
        # Create sample data
        data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})

        # Call the ShowPlot method
        result = self.plotter.ShowPlot('x', 'y', data)

        # Assert that the result is None
        self.assertTrue(result)

    def test_ShowPlotwithHue(self):
        # Create sample data
        data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50], 'hue': ['A', 'B', 'A', 'B', 'A']})

        # Call the ShowPlot method with hue
        result = self.plotter.ShowPlot('x', 'y', data, hue='hue')

        # Assert that the result is None
        self.assertTrue(result)
