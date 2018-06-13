#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

nx = 41
leng = 0.02
dx = leng / (nx - 1)
nt = 50000
rho = 2000
cp = 1500
k = 0.5

dt = (rho * cp * dx ** 2 / (2 * k)) * 0.1

print("dt = " + str(dt))

Tb = 280  # Temperature boundary

T = np.ones(nx)
T += 315

# print ("T " + str(T))

ap = rho * cp * dx / dt
ae = k / dx
plt.figure()
for tt in range(nt):
    TT = T.copy()
    T[-1] = ae * (TT[-2] - TT[-1]) / ap + TT[-1]  # pt right insul.
    T[0] = ((2 * ae * (Tb - TT[0])) - ae * (TT[0] - TT[1])
            ) / ap + TT[0]  # pt left T = 280
    for xx in range(1, nx - 1):  # eq pts centre
        T[xx] = ae * (TT[xx + 1] + TT[xx - 1] - 2 * T[xx]) / ap + TT[xx]

    if tt % 3000 == 0 or tt == 0 or tt == 200:
        print("T " + str(T))
        plt.plot(np.linspace(0, leng, nx), T,
                 label=("t = " + str(round(tt * dt)) + " s"))

plt.legend()
plt.show()
