import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.special import erf

# Define the integrand function
def integrand(p, c, t):
    return np.exp(-p - c**2 * p**2 * t) * np.cos(p*0) 

# Define a function to perform the integral over p from 0 to infinity
def integral_u(c, t):
    result, _ = quad(integrand, 0, np.inf, args=(c, t))
    return result

# Define a range of c values and t values
c_values = np.linspace(1, 10, 10)

t_values = np.linspace(0.01, 5, 100)

# Initialize a plot
plt.figure(figsize=(10, 8))

# Calculate and plot the integral for each c value
for c in c_values:
    u_values = [integral_u(c, t) for t in t_values]
    plt.plot(t_values, u_values, label=f'c = {c}')

# Label the plot
plt.xlabel('t')
plt.ylabel('u(t)')
plt.title('Graph of u(t) for x=0 with varying c values')
plt.legend()
plt.grid(True)
plt.show()
