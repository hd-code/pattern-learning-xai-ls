from base import testFunc
import logic.pattern as p

# ------------------------------------------------------------------------------

testFunc(p.count_variables, [
    ([[]], 0),
    ([["a", "b"]], 0),
    ([["b", "b"]], 0),
    ([[0]], 1),
    ([["b", "b", 0]], 1),
    ([["b", 0, "b", 0]], 1),
    ([["b", 0, "b", 1]], 2),
    ([["b", 0, 0, 1]], 2),
    ([[0, "a", 0, 1, 2]], 3),
])

testFunc(p.has_variables, [
    ([[]], False),
    ([["a", "b"]], False),
    ([["a", 0, "b"]], True),
    ([["a", 0, "b", 1]], True),
    ([[0]], True),
])

testFunc(p.to_string, [
    ([[]], ""),
    ([["a", "b"]], "ab"),
    ([[0, 1]], "x₀x₁"),
    ([["a", 0, "b"]], "ax₀b"),
    ([["a", 0, "b", 1]], "ax₀bx₁"),
    ([["a", 0, "b", 0, 1, "c", 2, 3, 2, "d"]], "ax₀bx₀x₁cx₂x₃x₂d"),
    ([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], "x₀x₁x₂x₃x₄x₅x₆x₇x₈x₉x₁₀x₁₁"),
])

# ------------------------------------------------------------------------------

testFunc(p.learn_iterative, [
    (["abc"], ["a", "b", "c"]),
    (["abc", []], ["a", "b", "c"]),
    (["abc", ["a", "b", "c", "d"]], ["a", "b", "c"]),
    (["cba", ["a", "b", "c", "d"]], ["c", "b", "a"]),
    (["abc", ["a", "b"]], ["a", "b"]),
    (["abc", ["a", 0]], ["a", 0]),
    (["abc", ["a", "b", "c"]], ["a", "b", "c"]),
    (["abc", ["a", "b", "a"]], ["a", "b", 0]),
    (["bbb", ["a", "b", "a"]], [0, "b", 0]),
    (["bbc", ["a", "b", "a"]], [0, "b", 1]),
    (["bbc", ["a", 0, "c"]], [0, 1, "c"]),
    (["aabbaa", ["a", "b", 0, 0, "b", "a"]], ["a", 0, 1, 1, 0, "a"]),
    (["d", [0]], [0]),
])

testFunc(p.learn_set, [
    ([["a", "b", "c"]], [0]),
    ([["aaa", "bbb", "ad"]], ["a", "d"]),
    ([["aabbaa", "aaccaa", "bbbbbb"]], [0, 0, 1, 1, 0, 0]),
    ([["aabbaa", "aaccaa", "bbbbbb", "a"]], ["a"]),
    ([["aabbaa", "aaccaa", "bbbbbb", "acbcaa"]], [0, 1, 2, 3, 0, 0]),
])

# ------------------------------------------------------------------------------

testFunc(p.get_learning, [
    ([[], "abc", ["a", "b", "c"]], p.Learning.initial),
    ([[0], "a", [0]], p.Learning.final),
    ([[0], "abc", [0]], p.Learning.final),
    ([[0, "b", 0], "abcd", [0, "b", 0]], p.Learning.ignored),
    ([["a"], "ab", ["a"]], p.Learning.ignored),
    ([[0, 1], "abc", [0, 1]], p.Learning.ignored),
    ([["a", "b", "c"], "abc", ["a", "b", "c"]], p.Learning.unaltered),
    ([["a", 0, "c"], "abc", ["a", 0, "c"]], p.Learning.unaltered),
    ([[0, "b", 0], "aba", [0, "b", 0]], p.Learning.unaltered),
    ([["a", "b", "c"], "ab", ["a", "b"]], p.Learning.shortened),
    ([[0, "b", 1], "ab", ["a", "b"]], p.Learning.shortened),
    ([["a", "b", "c"], "aba", ["a", "b", 0]], p.Learning.generalized),
    ([["a", "b", 0, 0, "b", "a"], "aabbaa", ["a", 0, 1, 1, 0, "a"]],
        p.Learning.generalized),
])

# ------------------------------------------------------------------------------

testFunc(p.is_consistent, [
    ([["a", "a"], ["aa", "aa"]], True),
    ([["a", "a"], ["aa", "ab"]], False),
    ([["a", 0, "a"], ["aaa", "aba", "aaabbbasba", "agjusndgqa"]], True),
    ([["a", 0, "a"], ["aaa", "aba", "aaabbbasbb", "agjusndgqa"]], False),
    ([[0, 1, "d", 0], ["aada", "badb", "aaaaada", "abffdab"]], True),
    ([[0, 1, "d", 0], ["aada", "badb", "aaaaadb", "abffdab"]], False),
])

testFunc(p.check_words, [
    (
        [["a", "a"], ["aa", "ab", "ac", "ba"]],
        [("aa", True), ("ab", False), ("ac", False), ("ba", False)]
    ),
    (
        [["a", 0, "a"], ["aaa", "aba", "aaabbbasba", "agjusndgqb", "agjusndgqa"]],
        [("aaa", True), ("aba", True), ("aaabbbasba", True),
         ("agjusndgqb", False), ("agjusndgqa", True)]
    ),
    (
        [[0, 1, "d", 0], ["aada", "badb", "aaaaada", "abffdab", "aaaaadb"]],
        [("aada", True), ("badb", True), ("aaaaada", True),
         ("abffdab", True), ("aaaaadb", False)]
    ),
])

testFunc(p.check_word, [
    ([["a"], "a"], True),
    ([["a"], "b"], False),
    ([[0], "a"], True),
    ([[0], "abc"], True),
    ([[0], "abbabba"], True),
    ([["a", 0, "b"], "aab"], True),
    ([["a", 0, "b"], "abb"], True),
    ([["a", 0, "b"], "aaa"], False),
    ([["a", 0, "b"], "aaaab"], True),
    ([["a", 0, "b"], "aabab"], True),
    ([["a", 0, "b"], "aabba"], False),
    ([[0, "b", 0], "aba"], True),
    ([[0, "b", 0], "bbb"], True),
    ([[0, "b", 0], "bba"], False),
    ([[0, "b", 0], "abbbabb"], True),
    ([[0, "b", 0], "abbabb"], False),
    ([[0, 1, 0], "aba"], True),
    ([[0, 1, 0], "bbb"], True),
    ([[0, 1, 0], "abb"], False),
    ([[0, 1, 0], "baaaab"], True),
    ([[0, 1, 0], "abaaaab"], True),
    ([[0, 1, 0], "abaaaac"], False),
    ([["a", 0, "b", 0, 1, "a", "a", 0, "b"], "acbcdaacb"], True),
    ([["a", 0, "b", 0, 1, "a", "a", 0, "b"], "acbcdaadb"], False,
        "last variable does not match"),
    ([["a", 0, "b", 0, 1, "a", "a", 0, "b"], "abbbbbcaabbb"], True),
    ([["a", 0, "b", 0, 1, "a", "a", 0, "b"], "abbbbbabaaabbb"], True),
    ([["a", 0, "b", 0, 1, "a", "a", 0, "b"], "abbbbcaabb"], True),
    ([["a", 0, "b", 0, 1, "a", "a", 0, "b"], "bdd"], False),
])

# ------------------------------------------------------------------------------

testFunc(p.generate_all_words, [
    (
        [[0], {"a", "b"}, 3],
        {"a", "b",
         "aa", "ab", "ba", "bb",
         "aaa", "aab", "aba", "abb", "baa", "bab", "bba", "bbb"}
    ),
    (
        [["a", 0, "b"], {"a", "b"}, 2],
        {"aab", "abb", "aaab", "aabb", "abab", "abbb"}
    ),
    (
        [[0, "b"], {"a", "b", "c"}, 2],
        {"ab", "bb", "cb",
         "aab", "abb", "acb", "bab", "bbb", "bcb", "cab", "cbb", "ccb"}
    ),
    (
        [[0, "c", 1, 0], {"a", "b"}, 2],
        {"acaa", "bcab", "acba", "bcbb",
         "acaaa", "acaba", "acbaa", "acbba", "bcaab", "bcabb", "bcbab", "bcbbb",
         "aacaaa", "aacbaa", "abcaab", "abcbab", "bacaba", "bacbba", "bbcabb", "bbcbbb",
         "aacaaaa", "aacabaa", "aacbaaa", "aacbbaa", "abcaaab", "abcabab", "abcbaab", "abcbbab",
         "bacaaba", "bacabba", "bacbaba", "bacbbba", "bbcaabb", "bbcabbb", "bbcbabb", "bbcbbbb"}
    ),
])
