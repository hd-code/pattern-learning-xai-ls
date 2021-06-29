from typing import Callable

# ------------------------------------------------------------------------------


def _setup():
    import os
    dir = os.path.dirname(__file__)
    dir = os.path.join(dir, "..", "src")
    dir = os.path.abspath(dir)

    import sys
    sys.path.insert(0, dir)


_setup()


# ------------------------------------------------------------------------------


bold = '\033[1m'
underline = '\033[4m'

succ = '\033[92m'
warn = '\033[93m'
fail = '\033[91m'

end = '\033[0m'


# ------------------------------------------------------------------------------


def test(func: Callable):
    print("Test", func.__module__, ">", func.__name__)
    try:
        func()
        print(succ + "  success" + end)
    except Exception as e:
        print(fail + "  failed" + end)
        print("    error:", e)
    except:
        print(fail + "  failed" + end)


def testMany(func: Callable, cases: list[tuple]):
    print("Test", func.__module__, ">", func.__name__)
    for case in cases:
        msg = "(" + case + ")"
        try:
            func(*case)
            print(succ + "  success" + end, msg)
        except Exception as e:
            print(fail + "  failed" + end, msg)
            print("    error:", e)
        except:
            print(fail + "  failed" + end, msg)


# ------------------------------------------------------------------------------


TestCaseFunc = tuple[list[any], any, str]  # (args, return, comment)


def testFunc(func: Callable, cases: list[TestCaseFunc]):
    print("Test", func.__module__, ">", bold + func.__name__ + end)
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
            print(succ + "  success" + end, msg)
        else:
            print(fail + "  failed" + end, msg)
            if note:
                print("    note:", note)
            print("    want:", want)
            print("     got:", got)
