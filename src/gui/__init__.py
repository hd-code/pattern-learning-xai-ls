import PySimpleGUI as sg

import gui.header as _header
import gui.table as _table


from gui.base import Layout, window_config, theme_name as app_theme

app_title = "Lernen von Pattern-Sprachen nach Lange und Wiehagen"


def create_layout() -> Layout:
    layout = []
    layout += _header.header()
    layout += _table.table()
    return layout


def after_window_init(window: sg.Window):
    _table.after_window_init(window)