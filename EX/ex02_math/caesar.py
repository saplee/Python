"""Caesar  cipher."""


def encode(word, shift):
    """"Encode a message using a Caesar cipher."""
    string = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in word:
        if letter.isalpha():
            number = (string.index(letter))
            new_number = (number + shift) % 26
            result += string[new_number]
        else:
            result += letter

    return result


print(encode("i like turtles", 6))
print(encode("o roqk zaxzrky", 20))
print(encode("example", 1))
print(encode("don't change", 0))
print(encode('the quick brown fox jumps over the lazy dog.', 7))
