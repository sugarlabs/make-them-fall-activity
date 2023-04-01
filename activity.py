#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pygame
import sugargame
import sugargame.canvas
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolcombobox import ToolComboBox
from gettext import gettext as _
import main


class Activity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.max_participants = 1
        self.sound = True
        self.game = main.game()
        self.game.canvas = sugargame.canvas.PygameCanvas(
                self,
                main=self.game.run,
                modules=[pygame.display, pygame.font, pygame.mixer])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()
        self.build_toolbar()

    def build_toolbar(self):

        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(False)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        button = ToolButton('speaker-muted-100')
        button.set_tooltip(_('Sound'))
        button.connect('clicked', self.sound_control)
        toolbar_box.toolbar.insert(button, -1)

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()
        # Add a pause/resume button
        self.paused = False
        pause_icon = 'media-playback-pause-symbolic' if self.paused else 'media-playback-start-symbolic'
        self.pause_button = ToolButton(pause_icon)
        self.pause_button.set_tooltip(_('Pause'))
        self.pause_button.connect('clicked', self.pause_resume_control)
        toolbar_box.toolbar.insert(self.pause_button, -1)

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(False)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()
        

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()
        stop_button.connect('clicked', self._stop_cb)

        self.show_all()
     

    def sound_control(self, button):
        self.sound = not self.sound
        self.game.sound = self.sound
        if not self.sound:
            button.set_icon_name('speaker-muted-000')
            button.set_tooltip(_('No sound'))
        else:
            button.set_icon_name('speaker-muted-100')
            button.set_tooltip(_('Sound'))
    def pause_resume_control(self, button):
        self.paused = not self.paused
        if self.paused:
            self.game.pause()
            self.pause_button.set_icon_name('media-playback-start-symbolic')
            self.pause_button.set_tooltip(_('Resume'))
        else:
            self.game.resume()
            self.pause_button.set_icon_name('media-playback-pause-symbolic')
            self.pause_button.set_tooltip(_('Pause'))
    def _stop_cb(self, button):
        self.game.crashed = True
        if self.game.running_mode:
            self.game.running_mode.crashed = True
