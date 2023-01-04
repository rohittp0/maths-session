import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-poster')

# step size
signal_step = 0.001
h = 0.1
# define grid+9+
x = np.arange(0, 2*np.pi, signal_step)
x_cent = np.arange(h, 2*np.pi-h, h)
# compute function
y = np.cos(x)
y_cent = np.cos(x_cent)

central_diff = np.diff(y_cent) / h

x = x[:-1]
x_cent = x_cent[:-1]
# compute exact solution
exact_solution = -np.sin(x)

# Plot solution
plt.figure(figsize = (12, 8))
plt.plot(x_cent, central_diff, '--', label ='Approximation')
plt.plot(x, exact_solution, label = 'Exact solution')
plt.legend()
plt.show()

# Compute max error between
# numerical derivative and exact solution
max_error = max(abs(exact_solution[::int(h/signal_step)][3:] - central_diff))
print(max_error)
