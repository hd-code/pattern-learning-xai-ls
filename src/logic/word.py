WordSymbol = str  # just one character
Word = str  # string of characters
Words = list[str]


def get_shortest_words(words: Words) -> Words:
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


def get_alphabet(words: Words) -> Alphabet:
    result = set()
    for word in words:
        for symbol in word:
            result.add(symbol)
    return result
