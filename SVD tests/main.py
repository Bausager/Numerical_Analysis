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




#XtX = np.dot(np.transpose(X),X)

#XT = np.transpose(X)

n = len(X[1,:])

XtX = np.zeros([n, n])

for i in tqdm(range(n)):
    for j in range(n):
        XtX[j, i] = (np.dot(np.transpose(X[:,i]), X[:,j]))



#print(XtX - XtX1)

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



n1 = len(X[1,:])

#XtX1 = np.zeros([n1, n1], dtype=float)

# for i in tqdm(range(n1)):
#     for j in range(n1):
#         XtX1[j, i] = (np.dot((X[:,i]), np.transpose(X[:,j])))


XtX1 = X @ np.transpose(X)

print(XtX1.shape)

s1, U1 = np.linalg.eig(XtX1)
S1 = np.diag(np.sqrt(s1))

print(S1)
print(U1)

VT1 = np.linalg.inv(S1) @ np.linalg.inv(U1) @ X
print(VT1)



#Xapprox = U[:,:r] @ S[:r,:r] @  np.transpose(V[:,:r])
#Xapprox = U @ S @ np.transpose(V)
Xapprox = U1 @ S1 @ VT1
print(Xapprox)
plt.figure(2)
img = plt.imshow(Xapprox)
img.set_cmap('gray')
plt.axis('off')
plt.title('Method of Snapshot: r = ' + str(r))





# Construct approximate image\n",
U1, S1, VT1 = np.linalg.svd(X,full_matrices=False)


S1 = np.diag(S1)
Xapprox = U1[:,:r] @ S1[0:r,:r] @ VT1[:r,:]
plt.figure(3)
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