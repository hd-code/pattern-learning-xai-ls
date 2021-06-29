import PySimpleGUI as sg

import event as ev
import pattern as pt


class App:
    def __init__(self):
        self.window: sg.Window

    def init(self):
        sg.theme("LightGrey6")
        layout = _create_layout()
        self.window = sg.Window(
            'Lernen von Mustern nach Lange und Wiehagen',
            layout,
            element_padding=(0, 0),
            font=font_normal,
            margins=(10, 10),
            border_depth=3,
        )

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break

            ev.fire(self.window, event, values)

    def exit(self):
        if self.window:
            self.window.close()


# ------------------------------------------------------------------------------


Layout = list[list[sg.Element]]


def _create_layout() -> Layout:
    layout = []
    layout += _create_header()
    layout += _create_table()
    return layout


font_normal = ("Helvetica", 20)
font_small = ("Helvetica", 12)
font_heading = ("Helvetica", 30)


# Header -----------------------------------------------------------------------


def _create_header() -> Layout:
    return [
        [sg.Text("Headline", font=font_heading)],
        # [sg.Text("Mit dieser Anwendung kann ein..")],
        # [sg.HorizontalSeparator(pad=(0, 20))],
    ]


# Table ------------------------------------------------------------------------


key_table = "table"


def _create_table() -> Layout:
    layout = [[sg.Column(_create_table_header(), key=key_table)]]
    layout += _create_table_input(1)
    return layout


props_id = {"size": (3, 1), "justification": "right"}


def _create_table_header() -> Layout:
    return [
        [sg.HorizontalSeparator()],
        [
            sg.Text("", **props_id),
            sg.Text("Eingaben", key=f"word_0", size=(10, 1)),
            sg.Text("Pattern", key=f"pattern_0", size=(10, 1), metadata=[]),
            sg.Text("Konsistenz"),
            sg.Button("?", size=(1, 1), border_width=0, font=font_small),
        ],
        [sg.HorizontalSeparator()],
    ]


key_table_id = "table_id"
key_table_enter = "table_enter"
key_table_input = "table_input"


def _create_table_input(index: int) -> Layout:
    ev.register(key_table_enter, _handle_table_input)
    return [
        [
            sg.Text(f"{index}.", key=key_table_id, **props_id),
            sg.Input("", key=key_table_input, size=(10, 1),
                     focus=True, metadata=index),
            sg.Button(key=key_table_enter, bind_return_key=True,
                      visible=False),
        ],
        [sg.HorizontalSeparator()],
    ]


def _handle_table_input(window: sg.Window, event: ev.EventName, values):
    word: str = values[key_table_input]
    index: int = window[key_table_input].metadata

    last_pattern: pt.Pattern = window[f"pattern_{index - 1}"].metadata
    pattern = pt.learn_iterative(word, last_pattern)

    window.extend_layout(
        window[key_table],
        _create_table_row(index, word, pattern)
    )

    index += 1

    window[key_table_id].update(f"{index}.")
    window[key_table_input].update("")
    window[key_table_input].metadata = index


def _create_table_row(index: int, word: str, pattern: pt.Pattern) -> Layout:
    key_word = f"word_{index}"
    key_pattern = f"pattern_{index}"

    return [
        [
            sg.Text(f"{index}.", **props_id),
            sg.Text(word, key=key_word, size=(10, 1)),
            sg.Text(pt.to_string(pattern), key=key_pattern, metadata=pattern),
            sg.Button("?", size=(1, 1), font=font_small),
            sg.Column([], expand_x=True),
            sg.Button("check", font=font_small),
            sg.Text("", size=(6, 1)),
        ],
        [sg.HorizontalSeparator()],
    ]
