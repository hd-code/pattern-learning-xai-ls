"""Event System

This module provides a central event bus to decouple the app from the individual
modules. It is possible to register callback functions, that are executed when
a specific event is fired.
"""

from typing import Any, Callable

import PySimpleGUI as sg


# ------------------------------------------------------------------------------


EventName = str
EventListener = Callable[[sg.Window, EventName, Any], None]


def clear():
    """Remove all registered events"""
    _listener.clear()


def fire(window: sg.Window, event: EventName, values: Any):
    """Fires an event.

    All registrars will be notified immediately.
    """
    if _is_paused:
        return

    callbacks = _listener.get(event, [_unknown_event])
    for callback in callbacks:
        callback(window, event, values)


def pause():
    """Pauses all events until resumed."""
    global _is_paused
    _is_paused = True


def resume():
    """Resumes the event bus after pausing."""
    global _is_paused
    _is_paused = False


def register(event_name: EventName, callback: EventListener):
    """Register an event.

    Events are registered under a specific name with a callback that is executed
    when the event is fired.
    """
    if _listener.get(event_name) == None:
        _listener[event_name] = [callback]
    else:
        _listener[event_name].append(callback)


def unregister(event_name: EventName, callback: EventListener = None):
    """Removes a registered event."""
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
