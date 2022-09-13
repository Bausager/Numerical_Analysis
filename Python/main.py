import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd


import OwnLib as OL

df = pd.read_csv (r'GroundTruth.csv')
df1 = pd.read_csv (r'Inter.csv')


M = len(df.X)
X = np.linspace(start=-1.0, stop=1, num=M)
Y = 1./(1. + 25.*np.power(X, 2))



plt.plot(X, Y, label="Ground Truth")
plt.plot(df.X, df.Y,label="Ground Truth (C++)")

n = len(df1.x)
x = np.linspace(start=-1.0, stop=1, num=n)

print("Interpolation with", n, "Points.")


plt.figure(1)

plt.plot(df1.x, df1.y, marker='*', linestyle="None", label="C++ Interp")
dftime = pd.read_csv (r'time.csv')

print("Time[s] consumed in working on the C++ implementation: \t\t",dftime.time[0])


y1 = np.zeros(n)
start = time.time()
y1 = OL.lagrange_interp(X, Y, x)
end = time.time()
print("Time[s] consumed in working on the fast python implementation: \t",end - start)

plt.plot(x, y1, label = "Lagrange Polynomial - fast", marker='*', linestyle='None')

y2 = np.zeros(n)
start = time.time()
y2 = OL.lagrange_interp(X, Y, x, fast=0)
end = time.time()
print("Time[s] consumed in working on the slow python implementation: \t",end - start)
plt.plot(x, y2, label = "Lagrange Polynomial - slow", marker='*', linestyle='None')


plt.grid()
plt.legend()
plt.show()

