import util
import unittest
from Drawer import Drawer

class TestDrawer(unittest.TestCase):
    def setUp(self):
        self.drawer = Drawer()
        pass

    def test_DrawHisto(self):
        self.drawer.DrawHisto()
        # Test the DrawHisto method
        # Add your test code here
        pass

    def test_DrawBoxPlot(self):
        self.drawer.DrawBoxPlot(110, 120)
        # Test the DrawBoxPlot method
        # Add your test code here
        pass

if __name__ == '__main__':
    unittest.main()

