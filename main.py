import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd


#import OwnLib as OL

df = pd.read_csv (r'GroundTruth.csv')

df1 = pd.read_csv (r'lagrange_interp.csv')

df2 = pd.read_csv (r'cubic_spine_interp.csv')



plt.figure()



plt.plot(df1.x, df1.y, marker='.', linestyle="None", label="Lagrange Interp")

plt.plot(df2.x, df2.y, marker='.', linestyle="None", label="Cubic Spline Interp")



plt.plot(df.X, df.Y,markersize=10, marker='*', linestyle="None", label="Ground Truth (C++)")


plt.ylim(-0.25, 1.5)
plt.grid()
plt.legend()
plt.show()

