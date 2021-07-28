# Problema 9. Incisos 9.3
import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(50, 15, 1000)
y = np.random.normal(110, 10, 1000)
z = np.random.normal(10, 5, 1000)
NBins = 50
xc = [10, 50, 110] 

fig, ax = plt.subplots(figsize = (10, 5))
ax.set_title("Histogramas de distribuciones normales diferentes")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.hist(x, NBins, facecolor = 'deeppink');
ax.hist(y, NBins, facecolor = 'darkblue');
ax.hist(z, NBins, facecolor = 'darkred');
for i in xc:
    ax.axvline(x = i, color = 'k', linestyle = '--')
plt.show()
