Alphabet = set[str]


def create(inputs: list[str]) -> Alphabet:
    result = set()
    for input in inputs:
        result = update(result, input)
    return result


def update(alphabet: Alphabet, input: str) -> Alphabet:
    result = alphabet.copy()
    for letter in input:
        result.add(letter)
    return result


def toString(alphabet: Alphabet) -> str:
    letters = list(alphabet)
    letters.sort()

    result = ""
    for letter in letters:
        result += letter
    return result
