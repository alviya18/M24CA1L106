#Write a pgm to perform numerical optimization to find the minimum of a given function using SciPy's optimization routines.
#Visualize the optimization path
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
def objective_function(x):
 return pow(x,2)
x0 = -2
result = minimize(objective_function, x0)
x = np.linspace(-5, 5, 50)
y = objective_function(x)
plt.plot(x, y)
plt.scatter(result.x, result.fun, color='green', label='Minimum Point')
plt.xlabel('x')
plt.ylabel('f(x)=x²')
plt.title('Numerical Optimization')
plt.grid(True)
plt.show()