from DataFusion import DataFusion
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt



class BoxPlotter:
    def __init__(self) -> None:
        self.data_fusion = DataFusion()

    def boxplot(self) -> None:
        # Get your data from DataFusion
        plt.figure(figsize=(10, 6))  # Adjust the size of the figure
        self.data_fusion.DataLoad()
        my_data = self.data_fusion.ExResultDataSet

        my_data = my_data[my_data["Set Number"] >= 140]
        my_data = my_data[145 >= my_data["Set Number"]]

        sns.boxplot(x="Set Number", y="Celsius", data=my_data, hue="Sensor")
        plt.show()

    def histo(self) -> None:
        plt.figure(figsize=(12, 10))
        # Set seaborn style
        sns.set()
        sns.set_style("whitegrid")
        plt.rcParams['font.weight'] = 'bold'
        plt.rcParams['axes.labelweight'] = 'bold'
        
        sns.set_palette("dark")
        sns.set_context("talk")
        # Get your data from DataFusion
        self.data_fusion.DataLoad()
        my_data = self.data_fusion.ExResultDataSet

        # Plot the histogram for each sensor
        sns.histplot(data=my_data, x="Celsius", bins=10,
                     hue="Sensor", multiple="stack")
        plt.title("Histogram for Each Sensor", fontsize=30, weight='bold')  
        plt.xlabel("Celsius", fontsize=28)  # Adjust the font size of x-axis label
        plt.ylabel("Frequency", fontsize=28)
        plt.tick_params(labelsize=23)

        plt.show()



if (__name__ == "__main__"):
    BoxPlotter().histo()

