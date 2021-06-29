from typing import Any, Callable

import PySimpleGUI as sg


EventName = str
EventListener = Callable[[sg.Window, EventName, Any], None]


def register(event_name: EventName, callback: EventListener):
    if _listener.get(event_name) == None:
        _listener[event_name] = [callback]
    else:
        _listener[event_name].append(callback)


def fire(window: sg.Window, event: EventName, values: Any):
    callbacks = _listener.get(event, [_unknown_event])
    for callback in callbacks:
        callback(window, event, values)


def _unknown_event(_: sg.Window, event: EventName, values: Any):
    print("An unknown event was fired!")
    print("  Event:", event)
    print("  Values:", values)


_listener: dict[EventName, list[EventListener]] = dict()
