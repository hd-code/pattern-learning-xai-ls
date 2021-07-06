"""Defines patterns for a pattern-language.

The main data structure of this application.
"""

import enum
import itertools as it
import typing

import logic.word as w


# ------------------------------------------------------------------------------


# str => constant, int => variable
PatternSymbol = typing.Union[w.WordSymbol, int]
Pattern = list[PatternSymbol]


def count_variables(pattern: Pattern) -> int:
    """Returns the number of variables in a pattern."""
    vars = set()
    for pattern_symbol in pattern:
        if isinstance(pattern_symbol, int):
            vars.add(pattern_symbol)
    return len(vars)


def has_variables(pattern: Pattern) -> bool:
    """Returns true if there are variables in a pattern."""
    for pattern_symbol in pattern:
        if isinstance(pattern_symbol, int):
            return True
    return False


def to_string(pattern: Pattern) -> str:
    """Gives a string representation of a pattern."""
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
    """Do one learning step.

    The current pattern and the entered word are passed as arguments. The
    improved pattern is then returned.
    """
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


def learn_set(words: list[w.Word]) -> Pattern:
    """Learns a pattern from a whole list of words."""
    shortest_words = w.get_shortest_words(words)
    pattern = []
    for word in shortest_words:
        pattern = learn_iterative(word, pattern)
    return pattern


# ------------------------------------------------------------------------------


class Learning(enum.IntEnum):
    """The different "kinds" of learning that can appear."""
    initial = enum.auto()
    final = enum.auto()
    ignored = enum.auto()
    generalized = enum.auto()
    unaltered = enum.auto()
    shortened = enum.auto()


def get_learning(prev_pattern: Pattern, word: w.Word, next_pattern: Pattern) -> Learning:
    """Analyzes what kind of learning took place."""
    if prev_pattern == []:
        return Learning.initial

    if prev_pattern == [0]:
        return Learning.final

    if prev_pattern == next_pattern:
        if len(word) > len(prev_pattern):
            return Learning.ignored
        return Learning.unaltered

    if len(prev_pattern) == len(next_pattern):
        return Learning.generalized

    return Learning.shortened


# ------------------------------------------------------------------------------


def is_consistent(pattern: Pattern, words: list[w.Word]) -> bool:
    """Returns true if a pattern generates all given words."""
    for word in words:
        if not check_word(pattern, word):
            return False
    return True


def check_words(pattern: Pattern, words: list[w.Word]) -> list[tuple[w.Word, bool]]:
    """Checks a list of words against a pattern.

    Returns a list of tuples containing the word and a bool, which is true when
    the pattern can generate this word.
    """
    result = []
    for word in words:
        result.append((word, check_word(pattern, word)))
    return result


def check_word(pattern: Pattern, word: w.Word) -> bool:
    """Checks a single word against a pattern.

    This function tries different combinations of variable lengths against the
    word. This is most performant for checking single words.
    """
    if not has_variables(pattern):
        return "".join(pattern) == word

    num_of_vars = count_variables(pattern)
    max_var_len = len(word) - len(pattern) + 1
    if max_var_len < 1:  # variables cannot be empty
        return False

    var_len_combis = _get_var_len_combis(num_of_vars, max_var_len)
    for var_len_combi in var_len_combis:
        if _check_var_len_combi(word, pattern, var_len_combi):
            return True

    return False


def _get_var_len_combis(num_of_vars: int, max_var_len: int) -> list[tuple[int]]:
    return list(it.product(range(1, max_var_len + 1), repeat=num_of_vars))


def _check_var_len_combi(word: w.Word, pattern: Pattern, var_len_combi: tuple[int]) -> False:
    if _calc_word_len(pattern, var_len_combi) != len(word):
        return False

    var_values: dict[int, str] = dict()
    windex = 0

    for pattern_symbol in pattern:
        if isinstance(pattern_symbol, str):
            if pattern_symbol != word[windex]:
                return False
            else:
                windex += 1
        else:
            var_value = var_values.get(pattern_symbol)
            if not var_value:
                var_len = var_len_combi[pattern_symbol]
                var_values[pattern_symbol] = word[windex:windex+var_len]
                windex += var_len
            else:
                for word_symbol in var_value:
                    if word[windex] != word_symbol:
                        return False
                    windex += 1

    return True


def _calc_word_len(pattern: Pattern, var_len_combi: tuple[int]) -> int:
    result = 0
    for pattern_symbol in pattern:
        if isinstance(pattern_symbol, int):
            result += var_len_combi[pattern_symbol]
        else:
            result += 1
    return result


# ------------------------------------------------------------------------------


def generate_all_words(pattern: Pattern, alphabet: w.Alphabet, max_var_len: int) -> set[str]:
    """Generates all possible words from a pattern and an alphabet up to a
    specific number of characters for each variable (including all shorter
    combinations).

    The amount of generated words quickly explodes. So, use with care! For
    shorter lists of words it is usually better to check the consistency for
    each word individually. See `check_word`.

    :param max_var_len: The maximum number of characters for each variable.
    """
    chars = list(alphabet)
    num_of_vars = count_variables(pattern)
    combinations = _get_combinations(chars, num_of_vars, max_var_len)

    result = set()
    for combination in combinations:
        word = _replace_vars_with_chars(pattern, combination)
        result.add(word)

    return result


def _get_combinations(chars: list[str], num_of_vars: int, max_var_len: int) -> list[tuple[str]]:
    char_combinations = _get_char_combinations(chars, max_var_len)
    return it.product(char_combinations, repeat=num_of_vars)


def _get_char_combinations(elements: list[str], max_len_of_combi: int) -> list[str]:
    result = []
    for i in range(0, max_len_of_combi):
        products = list(it.product(elements, repeat=i+1))
        for product in products:
            result.append("".join(product))
    return result


def _replace_vars_with_chars(pattern: Pattern, chars: tuple[str]) -> str:
    result = ""
    for pattern_symbol in pattern:
        if isinstance(pattern_symbol, str):
            result += pattern_symbol
        else:
            result += chars[pattern_symbol]
    return result
