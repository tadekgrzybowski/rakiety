import pygame
import numpy
import matplotlib.pyplot as plt

#799.8320866667023
#799.8321333333689
#799.8321333333689




class Rocket():
    def __init__(self, engine_thrust, rocket_mass, destination, delta_czas, v_k):
        self.e_t = engine_thrust
        self.e_t_2 = engine_thrust
        self.r_m = rocket_mass
        self.x_k = destination
        self.d_t = delta_czas
        self.y = 0
        self.v = 0
        self.v_k = v_k
        self.g_a = -9.8 # przyspieszenie ziemskie
        self.r_a = 0 # przyspieszenie rakiety
        self.i = 0
        self.data = [self.d_t, [], [], self.r_a, []]
        
    def launch(self):
        while True:
            self.main_calc()
            self.check_event()
            self.append_data()
            if self.y > self.x_k + 5 or self.y < -5:
                break
            if self.i > 70000:
                break

    def main_calc(self):
        self.r_a = (self.e_t / self.r_m) + self.g_a
        self.v += self.r_a * self.d_t
        self.y += self.v * self.d_t

    def check_event(self):
        b_d = -(self.v**2) / (2 * self.g_a)
        l_d = -(self.v_k**2 - self.v**2) / (2 * ((self.e_t_2 / self.r_m) + self.g_a))
        if ((round(b_d) + round(self.y)) == self.x_k and self.e_t != 0):
            self.e_t = 0
        if round(self.y) - round(l_d) == 0 and self.v < 0:
            self.e_t = self.e_t_2
   
    def append_data(self):
        self.i += 1
        self.data[1].append(self.y)
        self.data[2].append(self.v)
        self.data[4].append(self.i * self.d_t)

    def plot(self):
        plt.plot(self.data[1])
        plt.ylabel("X(t)")
        plt.xlabel("t*20")
        plt.show()

if __name__ == '__main__':
    rocket = Rocket(35000000, 3000000, 800, 0.001, 1)
    rocket.launch()
    rocket.plot()
