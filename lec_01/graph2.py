import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 10.01, 0.01)

plt.plot(np.log((x*x + 1)*np.e**( -(np.abs(x)/10) ))/np.log(1 + np.tan(1/(1 + (np.sin(x))**2))))

plt.show()

#(np.log((x*x + 1)*np.e( -(np.abs(x)/10) ))/np.log(1 + np.tan(1/(1 + (np.sin(x))**2))))