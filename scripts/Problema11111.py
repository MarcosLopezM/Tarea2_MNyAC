import matplotlib.pyplot as plt
import numpy as np


class position:

    def __init__(self, omega, Xm = 1, phi = 0):
        self.omega = omega 
        self.Xm = Xm
        self.phi = phi 
    
    def mass1(self, t):
        m1 = self.Xm * np.cos(self.omega * t + self.phi)
        return m1 
    
    def mass2(self, t):
        m2 = self.Xm * np.cos(2 * self.omega * t + self.phi)
        return m2

    def mass3(self, t):
        m3 = self.Xm * np.cos(3 * self.omega * t + self.phi)
        return m3

    def make_sim(self):
        t = np.linspace(0, 20, 1000)
        x1 = self.mass1(t)
        x2 = self.mass2(t)
        x3 = self.mass3(t)
        
        self.graphs(x1, x2, x3)

    def graphs(self, x1, x2, x3):
        
        t = np.linspace(0, 20, 1000)
        fig, ax=plt.subplots(figsize=(10,5))
        ax.set_title("Gráficas de x vs t para objetos con frecuencias naturales $\omega_{0},\, 2\omega_{0}\,y\,3\omega_{0}$")
        ax.set_xlabel('Tiempo (s)')
        ax.set_ylabel('Distancia (m)')
        ax.plot(t, x1, label = 'Obj. 1 con $\omega_{0}$', c = 'deeppink')
        ax.plot(t, x2, label = 'Obj. 1 con $2\omega_{0}$', c = 'b')
        ax.plot(t, x3, label = 'Obj. 1 con $3\omega_{0}$', c = 'r')
        ax.legend(bbox_to_anchor=(1, 1), loc='upper left');
        ax.set_xlim(0, 20)
        fig.tight_layout()
        fig.show()

post = position(omega = 0.5)
post.make_sim()
