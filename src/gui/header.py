"""The header area of the main window before the table."""

import PySimpleGUI as sg

from gui.base import Layout, expand, font_bold, font_heading, font_small
from gui.popup import popup
import event as ev


def header() -> Layout:
    ev.register(_key_info, _handle_info)
    return [
        [
            expand(),
            sg.Text("Lernen von Pattern-Sprachen",
                    font=font_heading, pad=(0, (0, 20))),
            sg.Button("?", key=_key_info, font=font_small,
                      pad=(0, (0, 20)), tooltip="Worum geht es?"),
            expand(),
        ],
    ]


# ------------------------------------------------------------------------------

_key_info = "header_info"


def _handle_info(*_):
    T = sg.Text
    C = sg.Column

    layout = [
        [T(_text_gen, size=(55, None))],
        [
            C([[T(_text_pat1, font=font_bold)]], vertical_alignment="top"),
            T(_text_pat2, size=(45, None)),
        ],
        [
            C([[T(_text_cons1, font=font_bold)]], vertical_alignment="top"),
            T(_text_cons2, size=(45, None)),
        ],
        [
            C([[T(_text_vars1, font=font_bold)]], vertical_alignment="top"),
            T(_text_vars2, size=(45, None)),
        ],
        [T(_text_ex, font=font_bold)],
        [T(_text_ex1)],
        [T(_text_ex2)],
    ]

    popup(_text_title, layout)


_text_title = "Über diese App"

_text_gen = "In dieser App kann eine Liste von Wörtern eingegeben werden. Eine KI versucht nun zu diesen Eingaben ein passendes beschreibendes Pattern zu finden."

_text_pat1 = "Patterns"
_text_pat2 = "sind Vorlagen zum Generieren von Wörtern. Sie bestehen aus Konstanten und Variablen."

_text_cons1 = "Konstanten"
_text_cons2 = "sind fixe Zeichen mit fester Position. Alle kleinen Buchstaben des Alphabets (a-z) sind in dieser App erlaubt."

_text_vars1 = "Variablen"
_text_vars2 = "können mit allen beliebigen Zeichenfolgen aus dem Alphabet gefüllt werden. Es muss aber mindestens ein Zeichen für eine Variable eingesetzt werden. Kommt eine Variable mehrmals im Pattern vor, so muss an den jeweiligen Stellen stets die gleiche Zeichenfolge eingesetzt werden. Variablen werden mit einem x plus einen Index dargestellt z.B. x₀, x₁ usw."

_text_ex = "Beispiele:"
_text_ex1 = """Pattern: ax₀c
Wörter:  aac, abc, abbc, aababc, ..."""
_text_ex2 = """Pattern: ax₀x₁x₀c
Wörter:  aabac, abcbc, abbcbbc, ..."""
