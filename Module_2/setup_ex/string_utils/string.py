def reverse(text):
    return text[::-1]


def only_vowels(text):
    return "".join([letter for letter in text if letter.lower() in "aeiouy"])


def only_consonants(text):
    return "".join([letter for letter in text if letter.lower() not in "aeiouy"])

