import pygame
import math
import time
pygame.init()

# Simualtion constants
MYPI = 3.14
COLOR_RED = (188, 39, 50)
COLOR_WHITE = (255, 255, 255)
SAMPLE_FREQ = 100  #100Hz
SAMPLE_PERIOD = 1 / SAMPLE_FREQ * 100
SAMPLE_POINTS = 700
AMPLITUDE = 10

# Main GUI window
root = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Signal genration simulation")

class Signal():
    def __init__(self, amplitude, phase, frequency, color, x_display_offset, y_display_offset):
        self.amplitude = amplitude
        self.phase = phase
        self.frequency = frequency
        self.color = color
        self.x_display_offset = x_display_offset
        self.y_display_offset = y_display_offset
        self.x = 0
        self.y = 0
        self.graf = []

    def update_points(self, step):
        w = self.frequency * 2 * 3.14
        t = step
        self.x = t
        self.y = self.amplitude * math.sin((w * t + self.phase))
        self.graf.append((self.x + self.x_display_offset, self.y + self.y_display_offset))

    def clear_graf(self):
        self.graf.clear()

    def draw(self):
        if len(self.graf) > 2:
            pygame.draw.lines(root, self.color, False, self.graf, 2)
            

class SinusSignal(Signal):
    pass


class ConstanteSignal(Signal):    
    def update_points(self, step):
        self.x = step
        self.y = self.amplitude
        self.graf.append((self.x + self.x_display_offset, self.y + self.y_display_offset))


def main():
    run_status = True
    simualtion_clock = pygame.time.Clock()
    i = 0
    simulation_signal_1 = SinusSignal(amplitude=30, phase=0, frequency=60, color=COLOR_RED, x_display_offset=50, y_display_offset=150)
    simulation_signal_2 = SinusSignal(amplitude=35, phase=30, frequency=30, color=COLOR_WHITE, x_display_offset=50, y_display_offset=250)
    simulation_signal_3 = ConstanteSignal(amplitude= 120, phase=0, frequency=0, color=COLOR_RED, x_display_offset=50, y_display_offset= 300)

    while run_status:
        simualtion_clock.tick(100)
        root.fill((0, 0, 0))
        simulation_signal_1.update_points(i * SAMPLE_PERIOD)
        simulation_signal_2.update_points(i * SAMPLE_PERIOD)
        simulation_signal_3.update_points(i * SAMPLE_PERIOD)
        #print(f"i is: {i + SAMPLE_PERIOD}, for sample period {SAMPLE_PERIOD}")
        i += 1

        if len(simulation_signal_1.graf) > 2:
            simulation_signal_1.draw()
            simulation_signal_2.draw()
            simulation_signal_3.draw()

        if i == SAMPLE_POINTS:
            i = 0
            simulation_signal_1.clear_graf()
            simulation_signal_2.clear_graf()
            simulation_signal_3.clear_graf()
            time.sleep(0.5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_status = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
