"""example of Fourier transform from I don't remember where"""
import numpy as np
import math
import matplotlib.pyplot as plt

pi = math.pi


def dft(f_n):
    N = len(f_n)
    f_k_re = np.zeros((N))
    f_k_im = np.zeros((N))
    k = 0
    while k < N:
        n = 0
        while n < N:
            f_k_re[k] += f_n[n] * np.cos(2.0 * pi * n * k / N)
            f_k_im[k] += f_n[n] * np.sin(2.0 * pi * n * k / N)

            n += 1
        k += 1
    return f_k_re, f_k_im


f0 = 5
N = 100  # nb samples (unit = unit! = discrete points) - not time!!!!
x = np.linspace(0, N, N)

y = np.sin(2 * pi * f0 * x)

dft_re, dft_im = dft(y)

plt.figure()
plt.plot(x, y, 'k-', label="freq = " + str(f0))
plt.title("f0 = " + str(f0))
plt.text(N * 1. / 3, 0, "if, for example, 100pts represent 10s: \
 \n frequency is N pts = n seconds, so f = 5 / 10 = 0.5 \
 \n because the peak is at 5 on the other graph")
plt.grid()
plt.legend()

plt.figure()
plt.plot(x, dft_re, 'b-', label='Re')
plt.plot(x, dft_im, 'g-', label='Im')
plt.grid()
plt.legend()
plt.title("f0 = " + str(f0) + " on the number of points considered")
plt.text(N * 1. / 3, 0, "to know the real frequency, do: \
 \n N pts = n seconds, so f = x_pic / n")
plt.show()
