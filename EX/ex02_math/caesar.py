def encode(word, shift):
    numbers = ([ord(c) + shift for c in word])
    return ([chr(i) for i in (numbers)])


print(encode("abc",1))
