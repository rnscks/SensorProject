import util

import unittest
from Plotters.PlotterFactory import PlotterFactory
from Plotters.BoxPlotter import BoxPlotter
from Plotters.LinePlotter import LinePlotter
from Plotters.HistoPlotter import HistPlotter

class TestPlotterFactory(unittest.TestCase):
    def test_create_plotter_box(self):
        factory = PlotterFactory()
        plotter = factory.CreatePlotter("box")
        self.assertIsInstance(plotter, BoxPlotter)

    def test_create_plotter_line(self):
        factory = PlotterFactory()
        plotter = factory.CreatePlotter("line")
        self.assertIsInstance(plotter, LinePlotter)

    def test_create_plotter_histo(self):
        factory = PlotterFactory()
        plotter = factory.CreatePlotter("histo")
        self.assertIsInstance(plotter, HistPlotter)

    def test_create_plotter_unknown(self):
        factory = PlotterFactory()
        with self.assertRaises(ValueError):
            factory.CreatePlotter("unknown")