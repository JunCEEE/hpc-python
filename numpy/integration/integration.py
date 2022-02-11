import numpy as np
import matplotlib.pyplot as plt

a = 0
b = np.pi / 2
dxs = np.linspace(1e-3,1e-1,100)
func = np.sin
divs = []
for dx in dxs:
    xi = np.arange(a, b + dx, dx)
    xi_p = (xi[1:] + xi[:-1]) / 2
    s_val = np.sum(func(xi_p) * dx)
    div = abs(s_val - 1.0)
    divs.append(div)
fig, ax = plt.subplots()
plt.plot(dxs, divs, "o-")
ax.invert_xaxis()
plt.show()
