# Copyright (C) 2023 Riya Jain
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Riya Jain   riya1jain567@gmail.com


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
