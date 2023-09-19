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


from fallitem import FallItem
from random import randint


class Generator:

    def __init__(self):
        self.items_config = []
        self.items = []
        self.type = "spike"

    def configure(self, config, _type = "spike"):
        self.type = _type
        self.items = []
        self.items_config = config
        for _ in range(len(self.items_config)):
            self.items.append([])

    def generate(self, speed=7):
        for i, config in enumerate(self.items_config):
            if len(self.items[i]) < config[3]:
                side = int(randint(0, 1))
                self.items[i].append(FallItem(config[side][0],
                                            config[side][1],
                                            side, speed, config[2],
                                            _type = self.type))

    def update(self, guys=[]):
        for i, section_items in enumerate(self.items):
            for j, item in enumerate(section_items):
                for guy in guys:
                    if guy.check_collision(item.x, item.y,
                                           item.rect.width,
                                           item.rect.height):
                        if self.type == "spike":
                            return True
                        if self.type == "heart":
                            del self.items[i][j]
                    
                    if self.type == "heart" and \
                       guy.check_missed(item.y,
                                        item.rect.height):
                        del self.items[i][j]
                        return True
                        
                if item.update():
                    del self.items[i][j]
        return False
