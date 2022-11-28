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

r = 50

AtA = np.zeros([m, m], dtype=float)
for i in tqdm(range(m)):
    for j in range(m):
        AtA[j, i] = (np.dot(np.transpose(A[:,i]), A[:,j]))

s, V = np.linalg.eig(AtA)
S = np.diag(np.sqrt(s[:r]))

V = V[:,:r]
VT = np.transpose(V)

VS = np.dot(V, np.linalg.inv(S))
#print(V.shape)
#print(S.shape)
#print(VS.shape)

U = np.zeros([n,r])
for i in tqdm(range(n)):
    for j in range(r):
        U[i, j] = np.dot(A[i,:], VS[:,j])






AAt = np.zeros([n, n], dtype=float)
for i in tqdm(range(n)):
    for j in range(n):
        AAt[j, i] = (np.dot((A[i,:]), np.transpose(A[j,:])))

s1, U1 = np.linalg.eig(AAt)
S1 = np.diag(np.sqrt(s1))

U1_inv = np.linalg.inv(U1)
U1 = U1[:,:r]
S1 = S1[:r,:r]
S1_inv = np.linalg.inv(S1)


SU1 = np.dot(S1_inv, U1_inv)
SU1 = SU1.real

VT1 = np.zeros([r, m], dtype=float)
for i in tqdm(range(m)):
    for j in range(r):
        VT1[j, i] = np.dot(SU1[j,:], A[:,i])



plt.figure(1)
Xapprox = U @ S @ VT
img = plt.imshow(Xapprox)
img.set_cmap('gray')
plt.axis('off')
plt.title('Method(1) of Snapshot: r = ' + str(r))

plt.figure(2)
Xapprox = U1 @ S1 @ VT1
img = plt.imshow(Xapprox.real)
img.set_cmap('gray')
plt.axis('off')
plt.title('Method(2) of Snapshot: r = ' + str(r))

plt.figure(3)
# Construct approximate image\n",
U2, S2, VT2 = np.linalg.svd(A, full_matrices=False)
U3, S3, VT3 = np.linalg.svd(A, full_matrices=True)

S2 = np.diag(S2)
Xapprox = U2[:,:r] @ S2[:r,:r] @ VT2[:r,:]
img = plt.imshow(Xapprox)
img.set_cmap('gray')
plt.axis('off')
plt.title('r = ' + str(r))

print("Shape of U:", U.shape)
print("Shape of S:", S.shape)
print("Shape of V:", VT.shape)
print("===========")
print("Shape of U:", U1.shape)
print("Shape of S:", S1.shape)
print("Shape of V:", VT1.shape)
print("===========")
print("Shape of U:", U2.shape)
print("Shape of S:", S2.shape)
print("Shape of V:", VT2.shape)
print("===========")
print("Shape of U:", U3.shape)
print("Shape of S:", S3.shape)
print("Shape of V:", VT3.shape)
print("===========")

plt.show()
plt.close()