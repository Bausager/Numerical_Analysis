import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd


import interpolation as interp

M = 11
X = np.linspace(start=-1.0, stop=1, num=M)
Y = 1./(1. + 25.*np.power(X, 2))





n = 1000
x = np.linspace(start=-1.0, stop=1, num=n)
y = interp.lagrange_interp(X, Y, x)
y1 = interp.cubic_spine_interp(X, Y, x)



plt.figure(1)
plt.plot(x, y, marker='.', linestyle="None", label="lagrange_interp", alpha=1)
plt.plot(x, y1, marker='H', linestyle="None", label="cubic_spine", alpha=0.2)


plt.plot(X, Y, marker='*', linestyle="None", label="Ground Truth", markersize=10)
plt.grid()
plt.legend()
plt.show()

