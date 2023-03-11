# find the missing letter program

import string


def findIfMissingChar(givenLetter):
    characters = string.ascii_lowercase
    start = characters.index(givenLetter[0])
    for char in characters[start:]:
        if char not in givenLetter:
            return char
    return f"complete sentance "


print(findIfMissingChar(input()))
