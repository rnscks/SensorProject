from matplotlib import pyplot as plt    
import numpy as np
#
# Define a range for x
x = np.linspace(-5, 5, 400)

# Plotting the graph for different values of 'a' to widen the bell shape
plt.figure(figsize=(8, 6))

# Values of 'a' to control the width of the bell
a_values = [20, 30, 40, 50]

for a in a_values:
    # Wider bell curve
    y = 30 / (1 + (x/a)**2)
    plt.plot(x, y, label=f"epsilon = {a}", linewidth=3)
    

plt.xlabel("r", weight="bold", fontsize=20)
plt.ylabel("Celsius", weight="bold", fontsize=20)
plt.title("Initial Thermal Profile", fontsize=25, weight="bold")
plt.xticks(fontsize=15, weight="bold")
plt.yticks(fontsize=15, weight="bold")
plt.legend()
plt.grid(True)
plt.show()
