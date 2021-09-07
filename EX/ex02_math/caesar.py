def encode(shift):
    alphabet = "abcdefghijkmnopqrstuvwxyz"
    shifted_alphabet1= alphabet[shift:]
    shifted_alphabet2= alphabet[0:shift]
    shifted_alphabet= shifted_alphabet1+shifted_alphabet2




print(encode(2))