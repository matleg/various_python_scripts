#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

nx = 41
leng = 0.02
dx = leng / (nx - 1)
nt = 10000
rho = 2000
cp = 1500
k = 0.5

dt = 0.05  # (rho * cp * dx**2 / (2*k)) * 0.1

print("dt = " + str(dt))

Tb = 280  # Temperature boundary

T = np.ones((nx, 1))
T += 315
TT = T.copy()
buf = T.copy()
print("T_shape = " + str(T.shape) + " T " + str(T))

ap0 = rho * cp * dx / dt
ae = k / dx

matri = np.zeros((nx, nx))
matri[0, 0] = ap0 + ae + 2 * ae
matri[0, 1] = - ae
matri[-1, -1] = ae + ap0
matri[-1, -2] = -ae
a = range(nx)
# print ("a " + str(a))
matri[a[1:-1], a[1:-1]] = 2 * ae + ap0
matri[a[1:-1], a[:-2]] = -ae
matri[a[1:-1], a[2:]] = -ae

print("matri " + str(matri) + "\n matri_shape = " + str(matri.shape))

TT[0] = ap0 * T[0] + 2 * ae * Tb
TT[-1] = ap0 * T[-1]
TT[1:-1] = ap0 * T[1:-1]
print("TT " + str(TT) + "\n TT_shape = " + str(TT.shape))

tTT = TT.transpose()
# print ("tTT " + str(tTT) + "\n tTT_shape = "+ str(tTT.shape) )

plt.figure()

for tt in range(nt):
    T = np.hstack((T, buf))
    # print ("\n \n T_shape = "+ str(T.shape)+ " T " + str(T))
    # print ("TT " + str(TT) + "\n TT_shape = "+ str(TT.shape) )

    T[:, -1] = np.linalg.solve(matri, TT[:, -1])
    # print (" T " + str(T))

    if tt % 1000 == 0 or tt == 0 or tt == 100 or tt == 1000:
        print("T_last " + str(T[:, -1]) + " T_shape = " + str(T.shape))
        plt.plot(np.linspace(0, leng, nx), T[:, -1],
                 label=("t = " + str(round(tt * dt)) + " s"))

    TT[:, -1] = T[:, -1] * ap0
    TT[0, -1] = TT[0, -1] + 2 * ae * Tb

l = plt.legend()
l.draggable()

plt.show()
