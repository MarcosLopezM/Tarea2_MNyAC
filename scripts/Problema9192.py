# Problema 9. Incisos 9.1 y 9.2
import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(loc = 10, scale = 5, size = 1000)
y = np.random.normal(loc = 50, scale = 10, size = 1000)
z = np.random.normal(loc = 110, scale = 15, size = 1000)

fig, ax = plt.subplots(figsize = (10, 5))
ax.set_title("Histogramas de distribuciones normales diferentes")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.hist(x, bins = 'auto', facecolor = 'deeppink');
ax.hist(y, bins = 'auto', facecolor = 'darkblue');
ax.hist(z, bins = 'auto', facecolor = 'darkred');
plt.show()