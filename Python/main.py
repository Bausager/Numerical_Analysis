import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd


#import OwnLib as OL

df = pd.read_csv (r'GroundTruth.csv')
df1 = pd.read_csv (r'cubic_spine_interp.csv')


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




plt.grid()
plt.legend()
plt.show()

