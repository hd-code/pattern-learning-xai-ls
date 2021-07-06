"""Defines a word and helper functions for those words."""

WordSymbol = str  # just one character
Word = str  # string of characters


def get_shortest_words(words: list[Word]) -> list[Word]:
    """Returns a list of the shortest words from a longer list of words."""
    shortest_words = list()
    shortest_word_len = 999999999999999
    for word in words:
        word_len = len(word)

        if word_len < shortest_word_len:
            shortest_word_len = word_len
            shortest_words = list()

        if word_len == shortest_word_len:
            shortest_words.append(word)

    return shortest_words


# ------------------------------------------------------------------------------


Alphabet = set[WordSymbol]


def get_alphabet(words: list[Word]) -> Alphabet:
    """Extracts all appearing characters in a list of words."""
    result = set()
    for word in words:
        for symbol in word:
            result.add(symbol)
    return result
