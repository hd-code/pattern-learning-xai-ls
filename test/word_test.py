from base import testFunc
import logic.word as w


testFunc(w.get_shortest_words, [
    ([["aa", "ab", "bc", "aad", "abc"]], ["aa", "ab", "bc"]),
    ([["aaa", "aad", "aa", "abc", "ab", "bc"]], ["aa", "ab", "bc"]),
    ([["aadaab", "aaa", "aab", "abbc", "aabb", "abc"]], ["aaa", "aab", "abc"]),
    ([["aaa", "aad", "aa", "abc", "ab", "f", "bc"]], ["f"]),
    ([[]], []),
])

testFunc(w.get_alphabet, [
    ([["a", "b"]], {"a", "b"}),
    ([["cba"]], {"a", "b", "c"}),
    ([["abc", "bca", "cab"]], {"a", "b", "c"}),
    ([["aa", "ab", "bc", "aad", "abc"]], {"a", "b", "c", "d"}),
    ([["aaa", "aad", "aa", "abc", "ab", "bc"]], {"a", "b", "c", "d"}),
    ([["aaa", "aad", "aa", "abc", "ab", "f", "bc"]],
        {"a", "b", "c", "d", "f"}),
    ([[]], set()),
])
