import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-poster')

x = [x / 10 for x in range(30)]
y = np.log(x)
# define grid
# compute function

central_diff = np.diff(y)


# Plot solution
plt.figure(figsize = (12, 8))
plt.plot(x, y, '--', label ='Function')
plt.plot(x[:-1], central_diff, label = 'dy/dx')
plt.legend()
plt.show()

