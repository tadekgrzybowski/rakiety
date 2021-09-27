import pygame
import numpy
import matplotlib

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

    def launch(self):
        while True:
            self.main_calc()

    def main_calc(self):
        self.r_a = (self.e_t / self.r_m)
        self.v += self.r_a * self.d_t
        self.y += self.v * self.d_t + ((self.r_a / self.d_t**2) / 2)

    def check_event(self):
        b_d = self.y + self.v * (-self.v / -self.r_a) + ((-self.r_a*((-self.v / -self.r_a)**2)) / 2)
        if round(b_d, 2) + round(self.y, 2) == self.x_k:
            self.



if __name__ == '__main__':
    rocket = Rocket(35000000, 300000, 800, 0.01)