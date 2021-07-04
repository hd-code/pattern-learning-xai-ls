import PySimpleGUI as sg
import re

import event as ev
from gui.base import Layout, color_fail, color_succ, color_text, expand, font_bold, font_italic, font_small, size_text_block
from gui.popup import popup, popup_text
import logic.pattern as p


# ------------------------------------------------------------------------------


def table() -> Layout:
    layout = [[sg.Column(_header_row(), key=_key_table)]]
    layout += _input_row(1)
    return layout


def after_window_init(window: sg.Window):
    window[_key_input].set_cursor(cursor_color=color_text)


# ------------------------------------------------------------------------------


_key_table = "table"


class _KeysRow:
    def __init__(self, index: int):
        self.word = f"table_word_{index}"
        self.pattern = f"table_pattern_{index}"
        self.explain = f"table_explain_{index}"
        self.consistency = f"table_consistency_{index}"


def _extract_index_from_key(key: str) -> int:
    number = key.split("_")[-1]
    return int(number)


# HeaderRow --------------------------------------------------------------------


_props_id = {"size": (3, 1), "justification": "right"}
_props_cell = {"size": (15, 1)}
_props_quest = {"size": (1, 1), "font": font_small}


def _header_row() -> Layout:
    keys = _KeysRow(0)

    ev.register(_key_info_consistency, _handle_info_consistency)

    return [
        [sg.HorizontalSeparator()],
        [
            sg.Text("", **_props_id),
            sg.Text("Eingaben", key=keys.word, metadata="",
                    font=font_bold, **_props_cell),
            sg.Text("Pattern", key=keys.pattern, metadata=[],
                    font=font_bold, **_props_cell),
            sg.Text("Konsistenz", font=font_bold),
            sg.Button("?", key=_key_info_consistency,
                      tooltip="Was bedeutet Konsistenz?", **_props_quest),
        ],
        [sg.HorizontalSeparator()],
    ]


def _handle_info_consistency(*_):
    popup_text("Was bedeutet Konsistenz?", "Ein Pattern wird als konsistent bezeichnet, wenn alle bisher bekannten Wörter mit dem jeweiligen Pattern erzeugt werden können.\n\nLeider ist die Überprüfung, ob ein Wort durch ein Pattern erzeugt werden kann, ein np-vollständiges Problem. Dadurch kann der Konsistenz-Check etwas länger dauern in der Berechnung.")


# TableRow ---------------------------------------------------------------------


_key_info_consistency = "table_explain_consistency"


def _table_row(index: int, word: str, pattern: p.Pattern, learning) -> Layout:
    keys = _KeysRow(index)

    ev.register(keys.explain, _handle_explain_learn_step)
    ev.register(keys.consistency, _handle_check_consistency)

    return [
        [
            sg.Text(f"{index}.", **_props_id),
            sg.Text(word, key=keys.word, metadata=word, **_props_cell),
            sg.Text(p.to_string(pattern), key=keys.pattern, metadata=pattern),
            sg.Button("?", key=keys.explain, metadata=learning,
                      tooltip="Was hat der Algorithmus gemacht?", **_props_quest),
            expand(),
            sg.Button("check", key=keys.consistency, font=font_small,
                      tooltip="Check die Konsistenz der Eingaben."),
            sg.Text("", size=(7, 1)),
        ],
        [sg.HorizontalSeparator()],
    ]


def _handle_explain_learn_step(window: sg.Window, event: ev.EventName, _):
    index = _extract_index_from_key(event)
    keys = _KeysRow(index)

    learn_kind = window[keys.explain].metadata
    pattern_now = window[keys.pattern].metadata
    word = window[keys.word].metadata

    pattern_before = window[_KeysRow(index - 1).pattern].metadata

    size_left = (12, 1)

    (title, text) = _learn_explanation[learn_kind]
    layout = [
        [sg.Text(text, size=size_text_block)],
        [sg.HorizontalSeparator(pad=(0, 10))],
        [
            sg.Text("Pattern vorher:", size=size_left),
            sg.Text(p.to_string(pattern_before))
            if pattern_before else
            sg.Text("keins", font=font_italic),
        ],
        [
            sg.Text("Eingabe:", size=size_left),
            sg.Text(word),
        ],
        [
            sg.Text("Pattern jetzt:", size=size_left),
            sg.Text(p.to_string(pattern_now)),
        ],
    ]

    popup(title, layout)


_learn_explanation = {
    p.Learning.initial: (
        "Erste Eingabe",
        "Bisher gibt es nur ein einziges Wort. Daher ist das Wort auch gleich dem Pattern.",
    ),
    p.Learning.final: (
        "Universal-Pattern erreicht",
        "Mit dem Pattern x₀ kann jedes beliebige Wort generiert werden. Eine weitere Verfeinerung des Patterns ist nicht mehr möglich.",
    ),
    p.Learning.ignored: (
        "Eingabe ignoriert",
        "Das eingegebene Wort war zu lang und wurde deswegen ignoriert.",
    ),
    p.Learning.generalized: (
        "Pattern generalisiert",
        "Es wurden einige Konstanten durch Variablen ersetzt. Dadurch kann das Pattern nun mehr Wörter darstellen",
    ),
    p.Learning.unaltered: (
        "Eingabe wird bereits erzeugt",
        "Das eingegebene Wort kann bereits mit dem bisherigen Pattern erzeugt werden. Daher ist das Pattern gleich geblieben.",
    ),
    p.Learning.shortened: (
        "Pattern verkürzt",
        "Das eingegebene Wort war kürzer als alle vorherigen. Deshalb wurde auch das Pattern verkürzt, damit es dieses Wort darstellen kann.",
    ),
}


def _handle_check_consistency(window: sg.Window, event: ev.EventName, _):
    index = _extract_index_from_key(event)
    num_of_words = window[_key_input_id].metadata - 1

    max_word_len = 0
    words = []
    for i in range(num_of_words):
        word = window[_KeysRow(i + 1).word].metadata
        if max_word_len < len(word):
            max_word_len = len(word)
        words.append(word)

    pattern = window[_KeysRow(index).pattern].metadata

    checked_words = p.check_words(pattern, words)

    title = "Konsistenz-Check"
    layout = [
        [sg.Text("Pattern: "), sg.Text(p.to_string(pattern))],
        [sg.HorizontalSeparator(pad=(0, 10))],
    ]

    word_rows = []
    for checked_word in checked_words:
        word_rows.append([
            sg.Text(checked_word[0], size=(max_word_len, 1)),
            sg.Text("✓", text_color=color_succ)
            if checked_word[1] else sg.Text("x", text_color=color_fail),
        ])

    if index < num_of_words:
        layout += [[sg.Text("bisherige Eingaben:", font=font_small)]]
        word_rows.insert(index,
                         [sg.Text("spätere Eingaben:", font=font_small)])

    layout += word_rows
    popup(title, layout)


# InputRow ---------------------------------------------------------------------


_key_input_id = "table_input_id"
_key_input = "table_input"
_key_enter = "table_enter"


def _input_row(index: int) -> Layout:
    ev.register(_key_enter, _handle_input)
    return [
        [
            sg.Text(f"{index}.", key=_key_input_id,
                    metadata=index, **_props_id),
            sg.Input("", key=_key_input, focus=True, **_props_cell),
            sg.Button(key=_key_enter, bind_return_key=True, visible=False),
        ],
        [sg.HorizontalSeparator()],
        [sg.Text("Um ein Wort hinzuzufügen, bitte hier eingeben und ENTER drücken",
                 font=font_small)]
    ]


def _handle_input(window: sg.Window, _: ev.EventName, values):
    word: str = values[_key_input]

    if not word:
        return

    if not re.fullmatch("[a-z]{1,20}", word):
        popup_text(
            "Fehlerhafte Eingabe",
            "Ein Wort kann nur aus den kleinen Buchstaben a-z bestehen und darf nicht mehr als 20 Zeichen lang sein",
            True,
        )
        return

    index: int = window[_key_input_id].metadata

    prev_pattern: p.Pattern = window[_KeysRow(index - 1).pattern].metadata
    next_pattern = p.learn_iterative(word, prev_pattern)
    learning = p.get_learning(prev_pattern, word, next_pattern)

    window.extend_layout(
        window[_key_table],
        _table_row(index, word, next_pattern, learning)
    )

    index += 1

    window[_key_input_id].update(f"{index}.")
    window[_key_input_id].metadata = index
    window[_key_input].update("")
