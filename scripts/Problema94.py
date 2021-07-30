# Problema 9. Incisos 9.4
import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(loc = 10, scale = 5, size = 1000)
y = np.random.normal(loc = 50, scale = 10, size = 1000)
z = np.random.normal(loc = 110, scale = 15, size = 1000)
indices = list(range(1, 1001))
colors = ['deeppink', 'darkblue', 'darkred']


fig, ax = plt.subplots(figsize = (10, 5))
ax.scatter(indices, x, c = colors[0], label = "Distr. 1")
ax.scatter(indices, y, c = colors[1], label = "Distr. 2")
ax.scatter(indices, z, c = colors[2], label = "Distr. 3")
ax.set_title("Gráfica de dispersión de las diferentes distribuciones")
ax.legend()
plt.show()