# Problema 9. Incisos 9.3
import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(loc = 10, scale = 5, size = 1000)
y = np.random.normal(loc = 50, scale = 10, size = 1000)
z = np.random.normal(loc = 110, scale = 15, size = 1000)

fx, fy, fz = np.random.normal(size = 1000), np.random.normal(size = 1000), np.random.normal(size = 1000)
NBins = 50 

def normal(data, mu, sigma):
    return (1 / sigma * np.sqrt(2 * np.pi)) * np.exp((-0.5 * (x - mu) ** 2) / sigma ** 2)

fig, ax = plt.subplots(figsize = (10, 5))
ax.scatter(x, fx, c = 'k')
ax.scatter(y, fy, c = 'c')
ax.scatter(z, fz, c = 'deeppink')
plt.show()

