import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial



def lagrange_interp(X, Y, x, order=4, fast=True):

    if(order%2 != 0):
        return -1
    elif(order == 0):
        return -1
    else:
        pass

    """
        Parameters
        ----------
        X : X-values of known data points.
        Y : y-values of known data points.
        
        x : x-values of interpolation points.
        ----------

        Returns
        -------
        y : y-values of interpolation points.

    """
    
    # Defining variables.
    N_points = X.shape[0]
    N_points_intp = x.shape[0]
    points_tmp = np.zeros(order+1)
    data_tmp = np.zeros(order+1)
    y = np.zeros(N_points_intp)
    idx = 0

    if(fast):

        for n in range(0, N_points_intp):
            
            idx_n = np.argmin(np.abs(X[:] - x[n]))
            idx_i = 0;
            
            #Lower Bound
            if(idx_n <= order/2):
                idx_i = 0;

            #Upper Bound
            elif(N_points-1 - idx_n <= (order/2)):
                idx_i = N_points - (order + 1)

            # Normal Operation
            else:
                idx_i = idx_n - int(order/2)

            # For loop.
            for j in range(order+1):
                p = 1
                for i in range(order+1):
                    if(j != i):
                        p *= ((x[n] - X[idx_i+i])/(X[idx_i+j] - X[idx_i+i]))
                y[n] += (Y[idx_i+j] * p)
    else:


        for i in range(0, N_points_intp):
            
            idx = np.argmin(np.abs(X[:] - x[i]))
            
            if idx <= order/2:
                points_tmp[:] = X[0:order+1]
                data_tmp[:] = Y[0:order+1]
                poly = lagrange(points_tmp, data_tmp)
                coef = Polynomial(poly.coef[::-1]).coef
                y[i] = Polynomial(coef)(x[i])
                
            elif idx > order/2 and N_points - idx > order/2:
            
                points_tmp[:] = X[idx-int(order/2):idx+int((order/2)+1)]
                data_tmp[:] = Y[idx-int(order/2):idx+int((order/2)+1)]
                poly = lagrange(points_tmp, data_tmp)
                coef = Polynomial(poly.coef[::-1]).coef
                y[i] = Polynomial(coef)(x[i])
            else:
                points_tmp[:] = X[-(order+1):]
                data_tmp[:] = Y[-(order+1):]
                poly = lagrange(points_tmp, data_tmp)
                coef = Polynomial(poly.coef[::-1]).coef
                y[i] = Polynomial(coef)(x[i])

    return y 


