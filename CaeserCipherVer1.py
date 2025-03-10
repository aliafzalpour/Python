import string
alphabet = string.ascii_lowercase
direction = input("Type your 'encode' to encrypt, type 'decode' to decrypt:\n")
text = list(input("What is your message:\n").lower())
shift = int(input("Type the shift number:\n"))

def encode(text, shift):
    for i in range(0, len(text)):
        text[i] = alphabet[i + shift]
    text = ''.join(text)

def decode(text, shift):
    for i in range(0, len(text)):
        text[i] = alphabet[i - shift]
    text = ''.join(text)



if direction == "encode":
    encode(text, shift)
else :
    decode(text, shift)

print(text)