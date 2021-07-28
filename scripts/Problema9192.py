# Problema 9. Incisos 9.1 y 9.2
import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(50, 15, 1000)
y = np.random.normal(110, 10, 1000)
z = np.random.normal(10, 5, 1000)
NBins = 50

fig, ax = plt.subplots(figsize = (10, 5))
ax.set_title("Histogramas de distribuciones normales diferentes")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.hist(x, NBins, facecolor = 'g');
plt.hist(y, NBins, facecolor = 'b');
plt.hist(z, NBins, facecolor = 'r');
plt.show()