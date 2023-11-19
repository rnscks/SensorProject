import unittest
import pandas as pd
from Plotters.LinePlotter import LinePlotter
from unittest.mock import patch     


class TestLinePlotter(unittest.TestCase):
    def setUp(self) -> None:
        self.plotter = LinePlotter()    
        return super().setUp()

    def test_CallShowPlot(self):
        # Create a sample dataframe
        data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})
        # Mock the super().ShowPlot method
        with patch.object(LinePlotter, 'ShowPlot') as mock_show_plot:
            # Call the ShowPlot method
            self.plotter.ShowPlot('x', 'y', data)

            # Assert that the super().ShowPlot method was called with the correct arguments
            mock_show_plot.assert_called_with('x', 'y', data)

    def test_ShowPlot(self):
        # Arrange
        x = "x"
        y = "y"
        data = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

        # Act
        result = self.plotter.ShowPlot(x, y, data)

        # Assert
        self.assertTrue(result)

    def test_ShowPlotwithHue(self):
        # Arrange
        x = "x"
        y = "y"
        hue = "category"
        data = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6], "category": ["A", "B", "A"]})

        # Act
        result = self.plotter.ShowPlot(x, y, data, hue)

        # Assert
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()