from typing import Callable


def _setup():
    import os
    dir = os.path.dirname(__file__)
    dir = os.path.join(dir, "..", "src")
    dir = os.path.abspath(dir)

    import sys
    sys.path.insert(0, dir)


_setup()


# ------------------------------------------------------------------------------


def testFunc(func: Callable, cases: list[tuple[list[any], any]]):
    print("Test", func.__module__, ">", func.__name__)
    for case in cases:
        input = case[0]
        want = case[1]

        msg = "("
        for arg in input:
            msg += str(arg) + ", "
        msg = msg[:-2] + ") => " + str(want)

        got = func(*input)
        if got == want:
            print("  success", msg)
        else:
            print("  failed", msg)
            print("    want:", want)
            print("     got:", got)
