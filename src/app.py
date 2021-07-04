import PySimpleGUI as sg

import event as ev
import gui


class App:
    def __init__(self):
        self.window: sg.Window

    def init(self):
        sg.theme(gui.app_theme)
        self.window = sg.Window(
            gui.app_title,
            gui.create_layout(),
            **gui.window_config,
        )
        gui.after_window_init(self.window)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break

            ev.fire(self.window, event, values)

    def exit(self):
        if self.window:
            self.window.close()
