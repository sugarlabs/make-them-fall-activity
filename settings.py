
import pygame
from gi.repository import Gtk
from gi.repository import Gdk
from button import Button


def color_parse(color):
    rgba = Gdk.RGBA()
    rgba.parse(color)
    return (int(rgba.red * 255), int(rgba.green * 255), int(rgba.blue * 255))


class settings:

    def run(self, gameDisplay, bg_dimensions, offset, config):
        black = color_parse("black")
        bg_color = color_parse("beige")
        clock = pygame.time.Clock()

        self.gameDisplay = gameDisplay
        self.go_back = False
        self.config = config

        self.buttons = []

        font_path = "fonts/arial.ttf"
        font1 = pygame.font.Font(font_path, 18)
        font2 = pygame.font.Font(font_path, 44)

        # Buttons
        self.buttons.append(Button(offset[0] + bg_dimensions[0] - 70, 45,
                                   "data/images/back.png",
                                   self.back_action,
                                   scale=(70, 40)))
        self.buttons.append(Button(offset[0] + bg_dimensions[0] / 2, 160,
                                   "data/images/button-difficulty.png",
                                   self.change_difficulty,
                                   text=font1.render("Normal", True, black)))

        title = font2.render("SETTINGS", True, black)

        while self.running:
            # Gtk events
            while Gtk.events_pending():
                Gtk.main_iteration()
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                return

            gameDisplay.fill(black)

            # Draw background
            pygame.draw.rect(gameDisplay, bg_color, pygame.Rect(offset[0],
                             offset[1], bg_dimensions[0], bg_dimensions[1]))
            self.blit_centre(title, offset[0] + bg_dimensions[0] / 2, 50)

            if self.go_back:
                return

            # Update difficulty text in button
            self.buttons[1].text = font1.render(["Easy", "Normal", "Hard"]
                                                [self.config["difficulty"]],
                                                True, black)

            for btn in self.buttons:
                btn.update()

            pygame.display.update()
            clock.tick(60)

    def back_action(self):
        self.go_back = True

    def blit_centre(self, surf, x, y):
        rect = surf.get_rect()
        centered_coords = (x - rect.width // 2, y - rect.height // 2)
        self.gameDisplay.blit(surf, centered_coords)

    def change_difficulty(self):
        self.config["difficulty"] = (self.config["difficulty"] + 1) % 3
