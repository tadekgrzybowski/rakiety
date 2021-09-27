import pygame
import numpy
import matplotlib.pyplot as plt

class Rocket():
    def __init__(self, engine_thrust, rocket_mass, destination, delta_czas):
        self.e_t = engine_thrust
        self.r_m = rocket_mass
        self.x_k = destination
        self.d_t = delta_czas
        self.y = 0
        self.v = 0
        self.g_a = 10 # przyspieszenie ziemskie
        self.r_a = 0 # przyspieszenie rakiety
        self.i = 0
        self.data = [self.d_t, [], [], self.r_a, []]

    def launch(self):
        while True:
            self.main_calc()
            self.check_event()
            self.append_data()
            if self.y > self.x_k or self.y < 0:
                break

    def main_calc(self):
        self.r_a = (self.e_t / self.r_m) - self.g_a
        self.v += self.r_a * self.d_t
        self.y += self.v * self.d_t + ((self.r_a / self.d_t**2) / 2)

    def check_event(self):
        b_d = self.y + self.v * (-self.v / -self.r_a) + ((-self.r_a*((-self.v / -self.r_a)**2)) / 2)
        if round(b_d, 2) + round(self.y, 2) == self.x_k:
            self.e_t = 0

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
    rocket = Rocket(35000000, 3000000, 800, 0.01)
    rocket.launch()
    rocket.plot()