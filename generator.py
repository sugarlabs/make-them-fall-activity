from spike import Spike
from random import randint


class Generator:

    def __init__(self):
        self.spikes_config = []
        self.spikes = []

    def configure(self, config):
        self.spikes = []
        self.spikes_config = config
        for _ in range(len(self.spikes_config)):
            self.spikes.append([])

    def generate(self, speed=7):
        for i, config in enumerate(self.spikes_config):
            if len(self.spikes[i]) < config[3]:
                side = int(randint(0, 1))
                self.spikes[i].append(Spike(config[side][0],
                                            config[side][1],
                                            side, speed, config[2]))

    def update(self, guys=[]):
        for i, section_spikes in enumerate(self.spikes):
            for j, spike in enumerate(section_spikes):
                for guy in guys:
                    if guy.check_collision(spike.x, spike.y,
                                           spike.rect.width,
                                           spike.rect.height):
                        return True
                if spike.update():
                    del self.spikes[i][j]
        return False
