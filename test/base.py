import os
import sys
from typing import Callable

# Setup ------------------------------------------------------------------------


dir = os.path.dirname(__file__)
dir = os.path.join(dir, "..", "src")
dir = os.path.abspath(dir)

sys.path.insert(0, dir)

print("Testing...\n")


# Globals ----------------------------------------------------------------------

verbose = sys.argv.__contains__("--verbose") or sys.argv.__contains__("-v")


bold = '\033[1m'
underline = '\033[4m'

succ = '\033[92m'
warn = '\033[93m'
fail = '\033[91m'

end = '\033[0m'


# Test Functions ---------------------------------------------------------------


def test(func: Callable):
    head_msg = ["Test", func.__module__, ">", func.__name__]
    head_printed = False
    if verbose:
        head_printed = True
        print(*head_msg)

    try:
        func()
        if verbose:
            print(succ + "  success" + end)
    except Exception as e:
        if not head_printed:
            head_printed = True
            print(*head_msg)
        print(fail + "  failed" + end)
        print("    error:", e)
    except:
        if not head_printed:
            head_printed = True
            print(*head_msg)
        print(fail + "  failed" + end)


def testMany(func: Callable, cases: list[tuple]):
    head_msg = ["Test", func.__module__, ">", func.__name__]
    head_printed = False
    if verbose:
        head_printed = True
        print(*head_msg)

    for case in cases:
        msg = "(" + case + ")"
        try:
            func(*case)
            if verbose:
                print(succ + "  success" + end, msg)
        except Exception as e:
            if not head_printed:
                head_printed = True
                print(*head_msg)
            print(fail + "  failed" + end, msg)
            print("    error:", e)
        except:
            if not head_printed:
                head_printed = True
                print(*head_msg)
            print(fail + "  failed" + end, msg)


TestCaseFunc = tuple[list[any], any, str]  # (args, return, comment)


def testFunc(func: Callable, cases: list[TestCaseFunc]):
    head_msg = ["Test", func.__module__, ">", bold + func.__name__ + end]
    head_printed = False
    if verbose:
        head_printed = True
        print(*head_msg)

    for case in cases:
        input = case[0]
        want = case[1]
        note = ""
        if len(case) > 2:
            note = case[2]

        msg = "("
        for arg in input:
            msg += str(arg) + ", "
        msg = msg[:-2] + ") => " + str(want)

        got = func(*input)
        if got == want:
            if verbose:
                print(succ + "  success" + end, msg)
        else:
            if not head_printed:
                head_printed = True
                print(*head_msg)

            print(fail + "  failed" + end, msg)
            if note:
                print("    note:", note)
            print("    want:", want)
            print("     got:", got)
