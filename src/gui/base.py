import PySimpleGUI as sg


Layout = list[list[sg.Element]]


color_fail = "#800"
color_succ = "#080"
color_text = "#000"


font_normal = ("Helvetica", 20)
font_italic = ("Helvetica", 20, "italic")
font_bold = ("Helvetica", 20, "bold")

font_small = ("Helvetica", 12)

font_heading = ("Helvetica", 30)


pad_none = (0, 0)


size_text_block = (55, None)


theme_name = "HD"


window_config = {
    "element_padding": pad_none,
    "font": font_normal,
    "margins": (10, 10),
    "border_depth": 3,
    "finalize": True,
}


# ------------------------------------------------------------------------------


def expand() -> sg.Column:
    return sg.Column([], expand_x=True)


# ------------------------------------------------------------------------------

sg.theme_add_new(theme_name, {
    'BACKGROUND': '#eee',
    'TEXT': '#000',
    'INPUT': '#fff',
    'TEXT_INPUT': '#000',
    'SCROLL': '#000',
    'BUTTON': ('#000', '#ddd'),
    'PROGRESS': ('#000', '#000'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
})
