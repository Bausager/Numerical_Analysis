import numpy as np



def lagrange_interp(X, Y, x, order=4):

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

    return y 


def cubic_spine_interp(X, Y, x, alpha=0, beta=0):
    """
        Parameters
        ----------
        X : X-values of known data points.
        Y : y-values of known data points.
        
        x : x-values of interpolation points.

        alpha : start condition (normally between 0 and 1)
        beta : end condition (normally between 0 and 1)
        ----------

        Returns
        -------
        y : y-values of interpolation points.

    """
    N_points = X.shape[0]

    y = np.zeros(x.shape[0])

    delta = np.zeros(N_points - 1)

    A = np.zeros((N_points-2, N_points-2))
    b = np.zeros(N_points-2)
    c = np.zeros(N_points)
    

    for i in range(len(delta)):
        delta[i] = X[i+1] - X[i]
    
    for i in range(A.shape[0]): # build tri-diagonal matrix
        if i == 0: # start condetion
            A[i,i] = ((delta[i])/6.0)*alpha + ((delta[i] + delta[i+1])/3.0) # b_tilde
            A[i,i+1] = delta[i+1]/6.0 # c
        if i == A.shape[0]-1: # end condetion
            A[i,i-1] = delta[i]/6 # a
            A[i,i] = ((delta[i] + delta[i+1])/3.0) + beta*(delta[i+1]/6.0) # b_tilde_tilde
        else:
            A[i,i-1] = delta[i]/6 # a
            A[i,i] = (delta[i] + delta[i+1])/3.0 # b
            A[i,i+1] = delta[i+1]/6.0 # c

        b[i] = (Y[i+2] - Y[i+1])/delta[i+1] - (Y[i+1] - Y[i])/delta[i]

    c = np.linalg.solve(A, b)
    c = np.append(c[0]*alpha, c)
    c = np.append(c, c[-1]*beta)

    for i in range(x.shape[0]):
        for j in range(N_points - 1):
            if (X[j] <= x[i] <= X[j+1]): # piecewise
                y[i] = c[j]/6. * (((X[j+1] - x[i])**3)/delta[j] - delta[j]*(X[j+1] - x[i])) +\
                    c[j+1]/6. * (((x[i] - X[j])**3)/delta[j] - delta[j]*(x[i] - X[j])) +\
                    Y[j] * (X[j+1] - x[i])/delta[j] + Y[j+1] * (x[i] - X[j])/delta[j]
    return y




    