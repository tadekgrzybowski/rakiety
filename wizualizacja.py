





import pygame
import numpy
import matplotlib.pyplot as plt
import pygame


pygame.init()
black=(0,0,0)
myFont = pygame.font.SysFont("Times New Roman", 24)
x_lenght = 1000
y_lenght = 900
screen = pygame.display.set_mode([x_lenght, y_lenght])

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
        
        self.autopilot = 0
        self.engine_on_percent = 100
        self.rocket = pygame.image.load('rocket.png')
        self.rocket_x_iv = 32
        self.rocket_y_iv = 70
        
    def launch(self):
        while True :
            f = open("logs.csv", "w")
            f.write("y, v, a, t\n")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.autopilot = 0
                    if event.key == pygame.K_a:
                        self.autopilot = 1	
                    if event.key == pygame.K_DOWN and self.autopilot == 0 and self.engine_on_percent > 0:
                        if self.engine_on_percent < 10:
                            self.engine_on_percent = 0
                        else:
                            self.engine_on_percent = self.engine_on_percent -10
                    if event.key == pygame.K_UP and self.autopilot == 0 and self.engine_on_percent < 100:
                        if self.engine_on_percent > 90:
                            self.engine_on_percent = 100
                        else:
                            self.engine_on_percent = self.engine_on_percent + 10                        
             

            f.write(str(self.y) + "," + str(self.v) + "," + str(self.r_a) + "," + str(self.i * self.d_t) + "\n")                        
            self.blit()
            self.main_calc()
            self.append_data()
            
            if self.autopilot == 1:
                self.check_event()
                self.engine_on_percent = round(self.e_t/self.e_t_2*100) 
            if self.autopilot == 0:
                self.e_t = self.e_t_2*self.engine_on_percent/100
    
            if self.y > self.x_k + 10 or self.y < 0:
                break
        f.close()

        
    def main_calc(self):
        self.r_a = (self.e_t / self.r_m) + self.g_a
        self.v += self.r_a * self.d_t
        self.y += self.v * self.d_t

    def check_event(self):
        b_d = -(self.v**2) / (2 * self.g_a)
        l_d = (self.v_k**2 -(-self.v**2)) / (2 * ((self.e_t_2 / self.r_m) + self.g_a))
        if b_d + self.y > self.x_k and self.e_t != 0 and self.v > 0:
            self.e_t = 0
        if (self.y - l_d) > 0 and self.v < 0 and (self.y - l_d) < (self.d_t * 100) or (l_d - self.y) > 0 and self.v < 0 and (l_d - self.y) < (self.d_t * 100):
            self.e_t = self.e_t_2
   
    def append_data(self):
        self.i += 1
        self.data[1].append(self.y)
        self.data[2].append(self.v)
        self.data[4].append(self.i * self.d_t)

    #def plot(self):
        #plt.plot(self.data[1])
        #plt.ylabel("X(t)")
        #plt.xlabel("t*20")
        #plt.show()

    def blit(self):
        screen.fill((255, 255, 255))
        screen.blit(self.rocket,(x_lenght/2-self.rocket_x_iv , y_lenght - self.y - self.rocket_y_iv)) 
        ystringprint = myFont.render("Y = ", 1, black)
        yintprint = myFont.render(str(round(self.y)), 1, black)
        vstringprint = myFont.render("V = ", 1, black)
        vintprint = myFont.render(str(round(self.v)), 1, black)
        autopilotstringprint = myFont.render("autopilot ", 1, black)
        autopilotintprint = myFont.render(str(self.autopilot), 1, black)
        engine_on_percent_stringprint = myFont.render("thrust(%)", 1, black)
        engine_on_percent_intprint = myFont.render(str(self.engine_on_percent), 1, black)
        screen.blit(ystringprint, (10, 10))
        screen.blit(yintprint, (55, 10))
        screen.blit(vstringprint, (10, 60))
        screen.blit(vintprint, (55, 60))
        screen.blit(autopilotstringprint, (10, 110))
        screen.blit(autopilotintprint, (100, 110))
        screen.blit(engine_on_percent_stringprint, (10, 160))
        screen.blit(engine_on_percent_intprint, (115, 160))
        
        pygame.display.update()
        
if __name__ == '__main__':
    rocket = Rocket(70000000, 3000000, 800, 0.005, 1)
    rocket.launch()
    #rocket.plot()
    
    
