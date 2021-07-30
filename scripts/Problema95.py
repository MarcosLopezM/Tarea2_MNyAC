# Problema 9. Incisos 9.5
import matplotlib.pyplot as plt
import numpy as np 

x = np.random.normal(loc = 10, scale = 5, size = 1000)
y = np.random.normal(loc = 50, scale = 10, size = 1000)
z = np.random.normal(loc = 110, scale = 15, size = 1000)
indices = list(range(1, 1001))
colors = ['deeppink', 'darkblue', 'darkred']
mu_n = [10, 50, 110]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (10, 5))
fig.suptitle('Gráficas', fontsize=16)

####################### Incisos 9.1 y 9.2 #######################
ax1.hist(x, bins = 'auto', facecolor = 'deeppink');
ax1.hist(y, bins = 'auto', facecolor = 'darkblue');
ax1.hist(z, bins = 'auto', facecolor = 'darkred');
ax1.set_title("Histogramas de distribuciones\n normales diferentes", fontsize = 'small')
ax1.set_xlabel("X")
ax1.set_ylabel("Y")

####################### Inciso 9.3 #######################
ax2.hist(x, bins = 'auto', color = colors[0]);
ax2.hist(y, bins = 'auto', facecolor = colors[1]);
ax2.hist(z, bins = 'auto', facecolor = colors[2]);
for i in mu_n:
    ax2.axvline(x = i, color = 'k', linestyle = '--')
ax2.set_title("Histogramas de distribuciones\n normales diferentes", fontsize = 'small')
ax2.set_xlabel("X")
ax2.set_ylabel("Y")

####################### Inciso 9.4 #######################
ax3.scatter(indices, x, c = colors[0], label = "Distr. 1")
ax3.scatter(indices, y, c = colors[1], label = "Distr. 2")
ax3.scatter(indices, z, c = colors[2], label = "Distr. 3")
ax3.set_title("Gráfica de dispersión\n de las diferentes distribuciones", fontsize = 'small')
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax3.legend()

plt.savefig("plots/problema95.pdf")
plt.tight_layout()
plt.show()