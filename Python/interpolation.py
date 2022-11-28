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
    y = np.zeros(N_points_intp)

    if(fast):
        print("Michelles lagrange")
        for n in range(0, N_points_intp):
            
            idx_n = np.argmin(np.abs(X[:] - x[n]))
            idx_i = 0
            
            #Lower Bound
            if(idx_n < (order/2)):
                idx_i = 0

            #Upper Bound
            elif(N_points-1 - idx_n < (order/2)):
                idx_i = int(N_points-1 - (order))

            # Normal Operation
            else:
                idx_i = idx_n - int((order/2))

            # For loop.
            for j in range(0, int(order+1)):
                #print(j)
                p = 1
                for i in range(0, int(order+1)):
                    if(j != i):
                        p *= (x[n] - X[idx_i+i])/(X[idx_i+j] - X[idx_i+i])
                y[n] += (Y[idx_i+j] * p)
                

    else:
        print("Chistoffers lagrange")

        points_tmp = np.zeros(order+1)
        data_tmp = np.zeros(order+1)

        idx = 0

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
    n_points = x.shape[0]

    y = np.zeros(x.shape[0])

    delta = np.zeros(N_points-1)

    A = np.zeros((N_points-2, N_points-2))
    b = np.zeros(N_points-2)
    c = np.zeros(N_points)
    
    

    for i in range(N_points-1):
        delta[i] = X[i+1] - X[i]
        #print(delta[i])

    for i in range(A.shape[0]): # build tri-diagonal matrix

        if i == 0: # start condetion
            
            
            A[i,i] = ((delta[i])/6.0)*alpha + ((delta[i] + delta[i+1])/3.0) # b_tilde
            A[i,i+1] = delta[i+1]/6.0 # c
            
        elif i == A.shape[0]-1: # end condetion

            A[i,i-1] = delta[i]/6.0 # a
            A[i,i] = ((delta[i] + delta[i+1])/3.0) + beta*(delta[i+1]/6.0) # b_tilde_tilde

        else:

            A[i,i-1] = delta[i]/6 # a
            A[i,i] = (delta[i] + delta[i+1])/3.0 # b
            A[i,i+1] = delta[i+1]/6.0 # c


        b[i] = (Y[i+2] - Y[i+1])/delta[i+1] - (Y[i+1] - Y[i])/delta[i]

    c = np.linalg.solve(A, b)
    c = np.append(c[0]*alpha, c)
    c = np.append(c, c[-1]*beta)
    #print(c)
    
    for i in range(n_points):
        for j in range(N_points - 1):

            if (X[j] <= x[i] <= X[j+1]): # piecewise
                y[i] = c[j]/6.0 * (((X[j+1] - x[i])**3)/delta[j]  - delta[j]*(X[j+1] - x[i])) \
                + c[j+1]/6.0 * (((x[i] - X[j])**3)/delta[j] - delta[j]*(x[i] - X[j])) \
                + Y[j] * (X[j+1] - x[i])/delta[j] + Y[j+1] * (x[i] - X[j])/delta[j]
    return y


def THD(x, y, n=25, b=50, fig=1):
    """
    Parameters
    ----------
    x : x-values of known data points.
    y : y-values of known data points.
    b : base/fundamental frequency for harmonics
    fig : plot figures, 0 or 1
    ----------

    Returns
    -------
    THD : THD-values of n with base of b.
    THDp : THD percentage of n with base of b.
    PF : Power Factor
    """
    L = len(y)
    N = int(np.floor(L/2))

    Yf = np.zeros(L, dtype=complex)
    rYf = np.zeros(N, dtype=float)

    Cn_pos = np.zeros(N-1, dtype=complex)
    Cn_neg = np.zeros(N-1, dtype=complex)

    an = np.zeros(N-1, dtype=float)
    bn = np.zeros(N-1, dtype=float)
    cn = np.zeros(N, dtype=float)

    phi = np.zeros(N-1, dtype=float)

    THD = np.zeros(n+1, dtype=float)

    Ts = x[1]-x[0]
    fs = 1/Ts
    Fc = fs/L
    Xf = np.arange(0, N)*Fc

    Yf = np.fft.fft(y, norm=None) / L

    Cn_pos = Yf[1:N]
    Cn_neg = np.flip(Yf[N+2:])

    an = np.real(Cn_pos + Cn_neg)
    bn = np.real(1j*(Cn_pos - Cn_neg))

    cn[0] = np.abs(Yf[0])
    cn[1:] = np.sqrt((an**2 + bn**2))

    phi = np.real(np.arctan(-bn/an))
    phi_base = phi[np.argmin(np.abs(Xf[:] - (b)))]
    DPF = np.cos(phi_base)


    rYf[0] = np.abs(Yf[0])
    rYf[1:N] = np.abs(Yf[1:N])*2

    for i in range(0, n+1):
        idx_n = np.argmin(np.abs(Xf[:] - (b*i)))
        THD[i] = rYf[idx_n]

    #THD = THD/np.sqrt(2)

    THDp = round((np.sqrt(np.sum((THD[2:n]**2))))/THD[1],3)

    PF = round(1/(np.sqrt(1 + THDp**2))*DPF,3)

    THD /= THD[1]

    if fig:
        f, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
        ax1.scatter(Xf, rYf)
        ax1.set_xlim(0, b*n+0.5)
        ax1.set_xticks(np.arange(0, b*n+0.5, step=b))  # Set label locations.
        ax1.set_title("FFT (peak domane)")
        ax1.set_ylabel("Magnitude")
        ax1.set_xlabel("Frequency [Hz]")
        ax1.grid()

        ax2.bar(np.linspace(1, len(THD)-1, len(THD)-1), THD[1:])
        ax2.set_xlim(0.5, n+0.5)
        ax2.set_xticks(np.arange(1, n+1, step=1))  # Set label locations.
        ax2.set_title(f"Harmonic Distortion (%THD: {100*THDp}, PF: {PF}, n = {n})")
        ax2.set_ylabel("Percentage pr. Harmonic [%]")
        ax2.set_xlabel("Harmonic Number [n]")
        ax2.grid()

        plt.show()

    return (THD, THDp, PF)
