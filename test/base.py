"""Base setup for test files.

Should be imported in every test file!

By default, only failed tests are printed to the console. With the flag
"--verbose" or "-v" all tests and their results are printed out.
"""

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
    """Executes a test function.

    A test fails when an exception is thrown during the execution of the
    function.
    """
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
    """Executes a test function for every set of arguments provided in a list.

    If an exception is thrown during one of the test cases, that case fails.
    """
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
    """Tests a pure function against a list inputs and expected outputs.

    Can be used to test pure functions. It passes the arguments of a test case
    to the method and compares the returned value against the expected outcome.
    """
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
