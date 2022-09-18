import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd




import interpolation as interp

M = 11
X = np.linspace(start=-np.pi/2, stop=np.pi/2, num=M)
X = np.sin(X)
Y = 1./(1. + 25.*np.power(X, 2))





n = 1000
x = np.linspace(start=-np.pi/2, stop=np.pi/2, num=n)
x = np.sin(x)




lagrange1 = interp.lagrange_interp(X, Y, x)
lagrange2 = interp.lagrange_interp(X, Y, x, fast=False)

cubic_spine = interp.cubic_spine_interp(X, Y, x)





plt.figure(1)

#plt.plot(x, lagrange1, marker='.', linestyle="None", label="lagrange_interp1", alpha=1)
#plt.plot(x, lagrange2, marker='.', linestyle="None", label="lagrange_interp2", alpha=1)

#from scipy.interpolate import lagrange
#from numpy.polynomial.polynomial import Polynomial
#poly = lagrange(X, Y)
#plt.plot(x, Polynomial(poly.coef[::-1])(x), label='Polynomial', marker='.', linestyle="None", alpha=0.1)


plt.plot(x, cubic_spine, marker='H', linestyle="None", label="cubic_spine", alpha=0.05)

plt.plot(X, Y, marker='*', linestyle="None", label="Ground Truth", markersize=10)
plt.ylim(-0.25, 1.5)
plt.grid()
plt.legend()
plt.show()

