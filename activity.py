#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pygame

from sugar3.activity.activity import Activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton

import sugargame.canvas

from gettext import gettext as _
from main import MakeThemFallGame


class MakeThemFallActivity(Activity):

    def __init__(self, handle):
        Activity.__init__(self, handle)
        self.max_participants = 1
        self.sound = True
        self.game = MakeThemFallGame()
        self.build_toolbar()
        self.game.canvas = sugargame.canvas.PygameCanvas(
                self,
                main=self.game.run,
                modules=[pygame.display, pygame.font, pygame.mixer])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        self.add_toolbar_separator(toolbar_box)

        button = ToolButton('speaker-muted-100')
        button.set_tooltip(_('Sound'))
        button.connect('clicked', self.sound_control)
        toolbar_box.toolbar.insert(button, -1)
        button.show()

        self.add_toolbar_separator(toolbar_box, expand=True)

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()
        stop_button.connect('clicked', self._stop_cb)

    def add_toolbar_separator(self, toolbar_box, expand=False):
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(expand)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

    def sound_control(self, button):
        self.sound = not self.sound
        self.game.config["muted"] = not self.game.config["muted"]
        if not self.sound:
            button.set_icon_name('speaker-muted-000')
            button.set_tooltip(_('No sound'))
        else:
            button.set_icon_name('speaker-muted-100')
            button.set_tooltip(_('Sound'))

    def _stop_cb(self, button):
        self.game.running = False
        if self.game.running_mode:
            self.game.running_mode.running = False
