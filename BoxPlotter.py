from DataFusion import DataFusion
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt


class BoxPlotter:
    def __init__(self) -> None:
        self.data_fusion = DataFusion()

    def boxplot(self) -> None:
        # Get your data from DataFusion
        self.data_fusion.DataLoad()
        my_data = self.data_fusion.ExResultDataSet

        # Remove data above 30
        my_data = my_data[my_data["Set Number"] >= 140]
        my_data = my_data[160 >= my_data["Set Number"]]

        sns.boxplot(x="Set Number", y="Celsius", data=my_data, hue="Sensor")
        plt.show()

    def histo(self) -> None:
        # Get your data from DataFusion
        self.data_fusion.DataLoad()
        my_data = self.data_fusion.ExResultDataSet

        # Plot the histogram for each sensor
        sns.histplot(data=my_data, x="Celsius", bins=10,
                     hue="Sensor", multiple="stack")
        plt.title("Histogram for each sensor")
        plt.show()


if (__name__ == "__main__"):
    BoxPlotter().histo()
