from pylab import *
from scipy import interpolate

tab = np.loadtxt("x_y_points.txt", skiprows=1)
print(tab)

x = tab[:, 0]
y = tab[:, 1]
print(x, y)

f = interpolate.interp1d(x, y, bounds_error=False)

xnew = np.arange(300, 773, 0.1)
ynew = f(xnew)  # use interpolation function returned by `interp1d`

plot(x, y, 'o', xnew, ynew, '-')
xlabel("x")
ylabel("y")
show()
