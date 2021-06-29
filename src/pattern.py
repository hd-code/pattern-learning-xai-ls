from typing import Union
import math

import word as w


# ------------------------------------------------------------------------------


PatternSymbol = Union[w.WordSymbol, int]  # str => constant, int => variable
Pattern = list[PatternSymbol]


def count_variables(pattern: Pattern) -> int:
    vars = set()
    for pattern_symbol in pattern:
        if isinstance(pattern_symbol, int):
            vars.add(pattern_symbol)
    return len(vars)


def has_variables(pattern: Pattern) -> bool:
    for pattern_symbol in pattern:
        if isinstance(pattern_symbol, int):
            return True
    return False


def to_string(pattern: Pattern) -> str:
    result = ""
    for pattern_symbol in pattern:
        if isinstance(pattern_symbol, str):
            result += pattern_symbol
        else:
            result += "x" + _sub(pattern_symbol)
    return result


_sub_num_dict = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def _sub(number) -> str:
    return str(number).translate(_sub_num_dict)

# ------------------------------------------------------------------------------


def learn_iterative(word: w.Word, pattern: Pattern = []) -> Pattern:
    result: Pattern = []

    if len(pattern) == 0 or len(word) < len(pattern):
        for word_symbol in word:
            result.append(word_symbol)
        return result

    if len(pattern) < len(word):
        return pattern

    found_variables: dict[tuple[w.WordSymbol, PatternSymbol], int] = dict()

    for i in range(len(word)):
        word_symbol = word[i]
        pattern_symbol = pattern[i]

        if isinstance(pattern_symbol, str) and word_symbol == pattern_symbol:
            result.append(pattern_symbol)
            continue

        symbol_pair = (word_symbol, pattern_symbol)
        variable_index = found_variables.get(symbol_pair)
        if variable_index == None:
            variable_index = len(found_variables)
            found_variables[symbol_pair] = variable_index

        result.append(variable_index)

    return result


def learn_set(words: w.Words) -> Pattern:
    shortest_words = w.get_shortest_words(words)
    pattern = []
    for word in shortest_words:
        pattern = learn_iterative(word, pattern)
    return pattern


# ------------------------------------------------------------------------------


def check_words(pattern: Pattern, words: w.Words) -> bool:
    for word in words:
        if not check_word(pattern, word):
            return False

    return True


def check_word(pattern: Pattern, word: w.Word) -> bool:
    if not has_variables(pattern):
        pattern_word = ""
        for pattern_symbol in pattern:
            pattern_word += pattern_symbol
        return pattern_word == word

    max_var_len = len(word) - len(pattern) + 1
    if max_var_len < 1:  # variables cannot be empty
        return False

    num_of_variables = count_variables(pattern)
    permutations = _get_permutations(num_of_variables, max_var_len, 1)
    for permutation in permutations:
        if _check_permutation(pattern, word, permutation):
            return True

    return False


# requires the pattern to be canonical!!!
def _check_permutation(pattern: Pattern, word: w.Word, permutation: list[int]) -> bool:
    word_len = len(word)
    pattern_len = len(pattern)

    pindex = 0
    windex = 0

    vars: list[str] = list()

    while (windex < word_len and pindex < pattern_len):
        pattern_symbol = pattern[pindex]

        if isinstance(pattern_symbol, str):
            if pattern_symbol != word[windex]:
                return False
            else:
                windex += 1
                pindex += 1
                continue

        num_of_chars_of_var = permutation[pattern_symbol]
        if windex + num_of_chars_of_var > len(word):
            return False

        word_part = word[windex:windex+num_of_chars_of_var]
        windex += len(word_part)  # for the next round
        pindex += 1               # for the next round

        if pattern_symbol >= len(vars):
            vars.append(word_part)
            continue

        var_value = vars[pattern_symbol]
        if word_part != var_value:
            return False

    return windex == word_len and pindex == pattern_len


def _get_permutations(num_of_entries: int, end: int, start: int = 0) -> list[list[int]]:
    num_of_kinds = end + 1 - start
    result = list()
    for i in range(num_of_kinds ** num_of_entries):
        row = list()
        for j in range(num_of_entries):
            value = math.floor(i / (num_of_kinds ** (num_of_entries - j - 1)))
            row.append(value % num_of_kinds + start)
        result.append(row)
    return result
