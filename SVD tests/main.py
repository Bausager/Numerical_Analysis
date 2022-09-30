from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import os

from tqdm import tqdm

plt.rcParams['figure.figsize'] = [16, 8]



plt.close()

plt.figure(1)
A = imread(os.path.join('.','','dog.jpg'))
X = np.mean(A, -1); # Convert RGB to grayscale\n",

img = plt.imshow(X)
img.set_cmap('gray')
plt.axis('off')


n = len(X[1,:])
XtX = np.zeros([n, n])
for i in tqdm(range(n)):
    for j in range(n):
        XtX[j, i] = (np.dot(np.transpose(X[:,i]), X[:,j]))

s, V = np.linalg.eig(XtX)
S = np.diag(np.sqrt(s))

r = 100
V = V[:,:r]
S = S[:r,:r]
VS = np.dot(V, np.linalg.inv(S))

U = np.zeros([len(X[:,0]),r])
for i in tqdm(range(len(X[:,0]))):
    for j in range(r):
        U[i, j] = np.dot(X[i,:], VS[:,j])


print(V.shape)
print(U.shape)
print(S.shape)

n1 = len(X[:,0])


XXt = np.zeros([n1, n1], dtype=float)
for i in tqdm(range(n1)):
    for j in range(n1):
        XXt[j, i] = (np.dot((X[i,:]), np.transpose(X[j,:])))
#XXt = np.dot(X, np.transpose(X))

s1, U1 = np.linalg.eig(XXt)
#s1 = s1[:len(X[0,:])]
#U1 = U1[:,:len(X[0,:])]



S1 = np.diag(np.sqrt(s1))
UT1 = np.linalg.inv(U1)

#S1 = S1.real
UT1 = UT1.real

# U1 = U1[:,:r]
# S1 = S1[:r,:r]


UX1 = np.zeros([len(X[:,0]),r])

for i in tqdm(range(len(X[:,0]))):
    for j in range(r):
        UX1[i, j] = np.dot(UT1[i,:], X[:,j])



#a = UT1 @ X
a = UX1

print(a)

ST1 = np.linalg.inv(S1)


VT1 = ST1[:r,:] @ a[:,:]

V1 = np.transpose(VT1)
U1 = np.transpose(UT1[:r,:])

print(V1.shape)
print(U1.shape)
print(S1.shape)

# #Xapprox = U[:,:r] @ S[:r,:r] @  np.transpose(V[:,:r])
# Xapprox = U @ S @ np.transpose(V)
Xapprox = U1 @ S1 @ VT1
plt.figure(2)
img = plt.imshow(Xapprox.real)
img.set_cmap('gray')
plt.axis('off')
plt.title('Method of Snapshot: r = ' + str(r))





# # Construct approximate image\n",
# U1, S1, VT1 = np.linalg.svd(X,full_matrices=False)


# S1 = np.diag(S1)
# Xapprox = U1[:,:r] @ S1[0:r,:r] @ VT1[:r,:]
# plt.figure(3)
# img = plt.imshow(Xapprox)
# img.set_cmap('gray')
# plt.axis('off')
# plt.title('r = ' + str(r))
plt.show()


# # U, S, VT = np.linalg.svd(X,full_matrices=False)
# # S = np.diag(S)

# j = 0
# for r in (5, 20, 100):
#  # Construct approximate image\n",
#      Xapprox = U[:,:r] @ S[0:r,:r] @ V[:r,:]
#      plt.figure(j+1)
#      j += 1
#      img = plt.imshow(Xapprox)
#      img.set_cmap('gray')
#      plt.axis('off')
#      plt.title('r = ' + str(r))
#      plt.show()