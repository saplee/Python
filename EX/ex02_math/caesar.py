def encode(shift):
    alphabet = "abcdefghijkmnopqrstuvwxyz"
    shifted_alphabet1 = alphabet[-shift:]
    shifted_alphabet2 = alphabet[:-shift]
    shifted_alphabet = shifted_alphabet1 + shifted_alphabet2
    return shifted_alphabet


print(encode(1))
