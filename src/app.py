"""The main application class."""

import PySimpleGUI as sg

import event as ev
import gui


class App:
    def __init__(self):
        self.window: sg.Window

    def init(self):
        """Initializes the gui.

        Should always be called first.
        """
        sg.theme(gui.app_theme)
        self.window = sg.Window(
            gui.app_title,
            gui.create_layout(),
            **gui.window_config,
        )
        gui.after_window_init(self.window)

    def run(self):
        """Starts the applications main loop.

        This method is exited when the main window is closed.
        """
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break

            ev.fire(self.window, event, values)

    def exit(self):
        """Clean up the apps' resources."""
        if self.window:
            self.window.close()
