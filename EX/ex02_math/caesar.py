"""Caesar cipher."""


def encode(word, shift):
    """"Encode a message using a Caesar cipher."""
    string = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in word:
        if letter.isalpha():
            numbers = (string.index(letter))
            new_number = (numbers + shift) % 26
            result += string[new_number]
        else:
            result += letter

    return result


print(encode("i like turtles", 6))  # -> o roqk zaxzrky
print(encode("o roqk zaxzrky", 20))  # -> i like turtles
print(encode("example", 1))  # -> fybnqmf
print(encode("don't change", 0))  # -> don't change
print(encode('the quick brown fox jumps over the lazy dog.', 7))
