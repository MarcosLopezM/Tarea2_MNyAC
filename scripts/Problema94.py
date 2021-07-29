# Problema 9. Incisos 9.3
import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(50, 15, 1000)
y = np.random.normal(110, 10, 1000)
z = np.random.normal(10, 5, 1000)
fx = np.random.normal(50, 15, 1000)
NBins = 50 

def normal(data, mu, sigma):
    return (1 / sigma * np.sqrt(2 * np.pi)) * np.exp((-0.5 * (x - mu) ** 2) / sigma ** 2)

fig, ax = plt.subplots(1, 2, figsize = (10, 5))
ax[0].scatter(x, fx)
ax[1].scatter(x, normal(x, 50, 15))
plt.show()

