import pygame
import numpy
import matplotlib.pyplot as plt

class Rocket():
    def __init__(self, engine_thrust, rocket_mass, destination, delta_t):
        self.e_t = engine_thrust
        self.r_m = rocket_mass
        self.x_k = destination
        self.d_t = delta_t
        self.v = 0
        self.a = 10 #grawitacja
        self.r_a = 0 # przyspieszienie rakiety
        self.y = 0 # polozenie w osi y
        self.i = 0
        self.data = [self.d_t, [], [], self.r_a, []]

    def launch(self):
        while True:
            self.calc()
            self.check_events()
            self.append_data()
            if self.y > self.x_k or self.y < 0:
                break


    def calc(self):
        self.r_a = self.e_t/self.r_m - self.a
        self.v += self.r_a * self.d_t
        self.y += self.v * self.d_t + (self.r_a * self.d_t**2) / 2

    def check_events(self):
        b_r = self.y + self.v * ((-self.v) / -self.a) + (self.a * self.d_t**2) / 2
        print(b_r, self.y)
        if round(b_r + self.y) == self.x_k:
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