from base import test
import event as e

# ------------------------------------------------------------------------------


event_name1 = "ev1"
event_calls1 = []

event_name2 = "ev2"
event_calls2 = []


def callback1(*_):
    event_calls1.append(True)


def callback2(*_):
    event_calls2.append(True)


# ------------------------------------------------------------------------------


def test_register_and_fire1():
    e.register(event_name1, callback1)
    e.fire(None, event_name1, None)
    assert len(event_calls1) == 1, "event was not called"

    e.fire(None, event_name1, None)
    assert len(event_calls1) == 2, "event was not called a second time"


def test_register_and_fire2():
    e.register(event_name2, callback2)
    e.fire(None, event_name2, None)
    assert len(event_calls2) == 1, "event was not called"

    e.fire(None, event_name2, None)
    assert len(event_calls2) == 2, "event was not called a second time"


def test_register_second_callback():
    e.register(event_name1, callback2)
    e.fire(None, event_name1, None)
    assert len(event_calls1) == 3, "callback1 was not called"
    assert len(event_calls2) == 3, "callback2 was not called"


def test_fire_unknown_event():
    e.fire(None, "something", None)


# ------------------------------------------------------------------------------


test(test_register_and_fire1)
test(test_register_and_fire2)
test(test_register_second_callback)
test(test_fire_unknown_event)
