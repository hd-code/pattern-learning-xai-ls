import patternlearner as pl

pl.printHello()

print("Hello")


def calcSquare(x: int) -> int:
    return x * x


print("Square of 3:", calcSquare(3))

alph = pl.extractAlphabet(["aa", "ab", "bbbc"])
print(pl.toString(alph))
