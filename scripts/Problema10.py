import matplotlib.pyplot as plt 
import numpy as np

t = np.linspace(-2, 2, 1000)
pol = 230 * t ** 4 + 18 * t ** 3 + 9 * t ** 2 - 221 * t - 9
trig = np.tan(np.pi * t) - 6


fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Gráficas de funciones', fontsize=16)

####################### Polinomio #######################
ax1.set_title("Gráfica del polinomio\n $230x^{4} + 18x^{3} + 9x^{2} - 221x - 9$", fontsize = 'small')
ax1.tick_params(axis = 'both', labelsize = 'small')
ax1.axhline(color='black', lw=0.5)
ax1.axvline(color='black', lw=0.5)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_xlim(-1, 1)
ax1.set_ylim(-120, 400)
ax1.plot(t, pol, c = 'deeppink')

####################### Función trigonométrica #######################
ax2.set_title("Gráfica de la función trigonométrica\n $\\tan(\pi x) - 6$", fontsize = 'small')
ax2.tick_params(axis = 'both', labelsize = 'small')
ax2.axhline(color='black', lw=0.5)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_xlim(0, 1)
ax2.set_ylim(-6, 5)
ax2.plot(t, trig, c = 'deeppink')

fig.savefig("plots/problema10.pdf")
fig.tight_layout()
fig.show()
