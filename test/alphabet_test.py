from base import testFunc
from alphabet import create, update

testFunc(create, [
    [[["a", "b"]], {"a", "b"}],
    [[["aaa", "aab"]], {"a", "b"}],
    [[["aba", "bab"]], {"a", "b"}],
    [[["a", "b", "c"]], {"a", "b", "c"}],
    [[["cba"]], {"a", "b", "c"}],
    [[["abc", "bca", "cab"]], {"a", "b", "c"}],
])

testFunc(update, [
    [[{"a", "b"}, "abc"], {"a", "b", "c"}],
    [[{"a", "c"}, "abc"], {"a", "b", "c"}],
    [[{"a", "b"}, "a"], {"a", "b"}],
    [[{"a", "b"}, "b"], {"a", "b"}],
])
