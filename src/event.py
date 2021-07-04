from typing import Any, Callable

import PySimpleGUI as sg


# ------------------------------------------------------------------------------


EventName = str
EventListener = Callable[[sg.Window, EventName, Any], None]


def clear():
    _listener.clear()


def fire(window: sg.Window, event: EventName, values: Any):
    if _is_paused:
        return

    callbacks = _listener.get(event, [_unknown_event])
    for callback in callbacks:
        callback(window, event, values)


def pause():
    global _is_paused
    _is_paused = True


def resume():
    global _is_paused
    _is_paused = False


def register(event_name: EventName, callback: EventListener):
    if _listener.get(event_name) == None:
        _listener[event_name] = [callback]
    else:
        _listener[event_name].append(callback)


def unregister(event_name: EventName, callback: EventListener = None):
    if not _listener.get(event_name):
        return

    if callback == None:
        del _listener[event_name]

    try:
        _listener[event_name].remove(callback)
        if len(_listener[event_name]) == 0:
            del _listener[event_name]
    except:
        return


# ------------------------------------------------------------------------------s


def _unknown_event(_: sg.Window, event: EventName, values: Any):
    print("An unknown event was fired!")
    print("  Event:", event)
    print("  Values:", values)


_is_paused = False
_listener: dict[EventName, list[EventListener]] = dict()
