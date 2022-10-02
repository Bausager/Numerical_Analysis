from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import os

from tqdm import tqdm

plt.rcParams['figure.figsize'] = [16, 8]

X = imread(os.path.join('.','','dog.jpg'))
A = np.mean(X, -1); # Convert RGB to grayscale\n",


n = len(A[:,0])
m = len(A[0,:])

print("n:", n)
print("m:", m)
plt.close()

#plt.figure(1)
#img = plt.imshow(X)
#img.set_cmap('gray')
#plt.axis('off')


AtA = np.zeros([m, m], dtype=float)
for i in tqdm(range(m)):
    for j in range(m):
        AtA[j, i] = (np.dot(np.transpose(A[:,i]), A[:,j]))

s, V = np.linalg.eig(AtA)
S = np.diag(np.sqrt(s))

r = 50
V = V[:,:r]
VT = np.transpose(V)
S = S[:r,:r]

VS = np.dot(V, np.linalg.inv(S))

U = np.zeros([n,r])
for i in tqdm(range(n)):
    for j in range(r):
        U[i, j] = np.dot(A[i,:], VS[:,j])


<<<<<<< HEAD

AAt = np.zeros([n, n], dtype=float)
for i in tqdm(range(n)):
    for j in range(n):
        AAt[j, i] = (np.dot((A[i,:]), np.transpose(A[j,:])))

s1, U1 = np.linalg.eig(AAt)
S1 = np.diag(np.sqrt(s1))

r = 50
U1_inv = np.linalg.inv(U1)
U1 = U1[:,:r]
S1_inv = np.linalg.inv(S1)
S1 = S1[:r,:r]

SU1 = np.dot(S1_inv, U1_inv)
SU1 = SU1.real

VT1 = np.zeros([r, m], dtype=float)
for i in tqdm(range(m)):
=======
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
>>>>>>> 731fe192ee78420212fac14c876a299eb70f2e02
    for j in range(r):
        VT1[j, i] = np.dot(SU1[j,:], A[:,i])



<<<<<<< HEAD

plt.figure(1)
Xapprox = U @ S @ VT
img = plt.imshow(Xapprox)
img.set_cmap('gray')
plt.axis('off')
plt.title('Method(1) of Snapshot: r = ' + str(r))

=======
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
>>>>>>> 731fe192ee78420212fac14c876a299eb70f2e02
plt.figure(2)
Xapprox = U1 @ S1 @ VT1
img = plt.imshow(Xapprox.real)
img.set_cmap('gray')
plt.axis('off')
plt.title('Method(2) of Snapshot: r = ' + str(r))

plt.figure(3)
# Construct approximate image\n",
U2, S2, VT2 = np.linalg.svd(A, full_matrices=False)
S2 = np.diag(S2)
Xapprox = U2[:,:r] @ S2[:r,:r] @ VT2[:r,:]
img = plt.imshow(Xapprox)
img.set_cmap('gray')
plt.axis('off')
plt.title('r = ' + str(r))
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