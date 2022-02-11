import numpy as np
import matplotlib.pyplot as plt

dx = 0.1
xi = np.arange(0, np.pi / 2 + dx, dx)
# xi = np.linspace(0, np.pi/2, 100)
diff_xi = (np.sin(xi+dx) - np.sin(xi-dx))/(2*dx)
plt.plot(xi,np.sin(xi),label="sin")
plt.plot(xi,diff_xi,label="fd")
plt.plot(xi,np.cos(xi),"o",label="cos")
plt.legend()
plt.show()
