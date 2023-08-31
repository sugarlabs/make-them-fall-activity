import pygame
from gi.repository import Gdk
from gi.repository import Gtk
from button import Button


def color_parse(color):
    rgba = Gdk.RGBA()
    rgba.parse(color)
    return (int(rgba.red * 255), int(rgba.green * 255), int(rgba.blue * 255))


class rules:

    def run(self, gameDisplay, bg_dimensions, offset):

        def back_action():
            self.press = 1

        self.press = 0
        screen_rect = gameDisplay.get_rect()
        width = bg_dimensions[0]
        height = screen_rect.height
        black = (0, 0, 0)
        bg_color = color_parse("#f8eddd")  # Derived from rulesbackground.png

        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        background = pygame.image.load("data/images/rulesbackground.png")
        back = pygame.image.load("data/images/back.png")

        bg_rect = background.get_rect()

        # To maintain the aspect ratio of the image we calculate width according to screen height
        bg_w = int(height * (bg_rect.width / bg_rect.height))
        background = pygame.transform.scale(background, (bg_w, height))
        bg_rect = background.get_rect()

        back = pygame.transform.scale(back, (70, 40))
        back_btn = Button(offset[0] + width - 45, 25, "data/images/back.png",
                          back_action, scale=[70, 40])

        sound = True

        while self.running:
            # Gtk events

            while Gtk.events_pending():
                Gtk.main_iteration()
            event = pygame.event.poll()
            # totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                return

            if (pygame.mouse.get_pressed())[0] == 1 and self.press == 0:
                self.press = 1
                return

            if event.type == pygame.MOUSEBUTTONUP:
                self.press = 0

            mos_x, mos_y = pygame.mouse.get_pos()

            gameDisplay.fill(black)
            # Draw background
            pygame.draw.rect(gameDisplay, bg_color, pygame.Rect(offset[0],
                             offset[1], bg_dimensions[0], screen_rect.height))

            gameDisplay.blit(background, (offset[0] + bg_dimensions[0] / 2 - bg_rect.width / 2,
                                          screen_rect.height - bg_rect.height))

            back_btn.draw()

            pygame.display.update()
            clock.tick(60)
