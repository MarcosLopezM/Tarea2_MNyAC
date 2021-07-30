# Problema 9. Incisos 9.3
import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(loc = 10, scale = 5, size = 1000)
y = np.random.normal(loc = 50, scale = 10, size = 1000)
z = np.random.normal(loc = 110, scale = 15, size = 1000)
mu_n = [10, 50, 110] 
colors = ['deeppink', 'darkblue', 'darkred']

fig, ax = plt.subplots(figsize = (10, 5))
ax.set_title("Histogramas de distribuciones normales diferentes")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.hist(x, bins = 'auto', color = colors[0]);
ax.hist(y, bins = 'auto', facecolor = colors[1]);
ax.hist(z, bins = 'auto', facecolor = colors[2]);
for i in mu_n:
    ax.axvline(x = i, color = 'k', linestyle = '--')
plt.show()