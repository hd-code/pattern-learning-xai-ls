"""Better popups than what PySimpleGui offers.

Defines popups, which are additional windows used to communicate with the user.
"""

import time

import PySimpleGUI as sg

import event as ev
from gui.base import Layout, expand, font_small, font_heading, window_config


def popup(title: str, layout: Layout):
    ev.pause()

    win = sg.Window(
        title,
        [*_make_title_row(title), *layout],
        modal=True,
        **window_config,
    )
    win.read()

    win.close()
    ev.resume()


def popup_text(title: str, text: str, exit_with_any_key=False):
    ev.pause()

    layout = []
    layout += _make_title_row(title)
    layout += [[sg.Text(text, size=(45, None))]]

    if exit_with_any_key:
        layout += [[
            expand(),
            sg.Text("Verlassen mit beliebiger Taste", font=font_small),
            expand(),
        ]]

    win = sg.Window(
        title,
        layout,
        modal=True,
        return_keyboard_events=exit_with_any_key,
        **window_config,
    )

    if exit_with_any_key:
        start = time.time()
        while time.time() - start < .3:
            win.read()
    else:
        win.read()

    win.close()
    ev.resume()


def _make_title_row(title: str) -> Layout:
    return [[expand(), sg.Text(title, font=font_heading), expand()]],
