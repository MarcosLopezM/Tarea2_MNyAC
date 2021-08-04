#2 Suponer que tenemos un objeto que oscila de acuerdo a la ecuación de 
#  movimiento antes planteada

import numpy as np
import matplotlib.pyplot as plt

class energias():

    def __init__(self, omega, Xm = 1, phi = 0):
        self.omega = omega 
        self.Xm = Xm 
        self.phi = phi 
        
    def kinetic(self, t):
        K = 0.5 * self.Xm * np.sin(self.omega * t + self.phi) ** 2  
        return K
        
    def potential(self, t):
        U = 0.5 * self.Xm * np.cos(self.omega * t + self.phi) ** 2
        return U
       
    def make_sim(self):

        t = np.linspace(0, 20, 1000)
        K = self.kinetic(t)
        U = self.potential(t)
        T = K + U
        
        self.graphs(K, U, T)


    def graphs(self, e1, e2, e3):
        
        t = np.linspace(0, 20, 1000)
        fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, figsize=(10,10))
        fig.suptitle('Gráficas de Energía', y = 1.0)

        ax1.plot(t, e1, c = 'b')
        ax1.set_title("Energía cinética")
        ax1.set_xlabel("Tiempo (s)")
        ax1.set_ylabel("Energía (J)")

        ax2.plot(t, e2, c = 'deeppink')
        ax2.set_title("Energía potencial")
        ax2.set_xlabel("Tiempo (s)")
        ax2.set_ylabel("Energía (J)")
        
        ax3.plot(t, e3, c = 'k')
        ax3.set_title("Energía potencial")
        ax3.set_xlabel("Tiempo (s)")
        ax3.set_ylabel("Energía (J)")
        
        fig.tight_layout(h_pad = 2)
        fig.show()

E = energias(omega = 2)
E.make_sim()