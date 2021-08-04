# 1 Hacer una imagen ue muestre la posición de tres diferentes objetos que 
# sigan la ecuación antes descrita con frecuencias naturales de w0, 2w0, 3w0
# Suponer que todos los objetos tienen la misma amplitud de oscilación y 
# la misma constante de fase.

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})


class oscilacion():
    """
    Clase que simula una masa en movimiento oscilatorio
    """
    def __init__(self, w, A=1, phi=np.pi/2):
        self.A = A
        self.phi = phi
        self.w = w
        

    def pos1_x(self, t):
        res1 = self.A * np.cos(self.w*t+self.phi)
        return res1
    
    def pos2_x(self, t):
        res2 = self.A * np.cos(2*self.w*t+self.phi)
        return res2
        
    def pos3_x(self, t):
        res3 = self.A * np.cos(3*self.w*t+self.phi)
        return res3 

    def make_sim(self):

        time_vec = np.linspace(0, 50, 150)
        x1 = self.pos1_x(time_vec)
        x2 = self.pos2_x(time_vec)
        x3 = self.pos3_x(time_vec)
        
        self.plot_results(x1, x2, x3)


    def plot_results(self, x1, x2, x3):
        
        time_vec = np.linspace(0, 50, 150)
        fig, ax=plt.subplots(figsize=(15,7))
        ax.set_xlabel('Tiempo(s)')
        ax.set_ylabel('Distancia(m)')
        plt.title('Gráfica 1.' )

        plt.plot(time_vec, x1, label='Objeto 1 con w', color="red")
        plt.plot(time_vec, x2, label="Objeto 2 con 2w", color="blue")
        plt.plot(time_vec, x3, label="Objeto 3 con 3w", color="green")
        plt.legend(loc='best')
        plt.xlim(0,50)

g1 = oscilacion(w=.25)
g1.make_sim()