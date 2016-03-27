import numpy as np

A = np.matrix('1, 2, 3; 2, 7, 4')

B = np.matrix('1, -1; 0, 1')

C = np.matrix('5, -1; 9, 1; 6, 0')

D = np.matrix('3, -2, -1; 1, 2, 3')


u = np.array([6, 2, -3, 5])

v = np.array([3, 5, -1, 4])

print("1. Matrix dimensions")

print("A: " + str(A.shape))
print("B: " + str(B.shape))
print("C: " + str(C.shape))
print("D: " + str(D.shape))
print("u: " + str(u.shape))
print("v: " + str(v.shape))

print("2. Vector operations")

print(".1 " + str(u+v))

print(".2 " + str(u-v))

print(".3 " + str(3*u))

print(".4 " + str(np.vdot(u, v)))

print(".5 " + str(np.linalg.norm(u)))


print("3. Matrix operations")

print(".1 not defined")

print(".2 " + str(A-C.getT()))

print(".3 " + str(C.getT()+3*D))

print(".4 " + str(B*A))

