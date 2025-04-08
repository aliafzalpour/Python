import string
alphabet = string.ascii_lowercase
direction = input("Type your 'encode' to encrypt, type 'decode' to decrypt:\n")
text = list(input("What is your message:\n").lower())
shift = int(input("Type the shift number:\n"))

def caeser(text, shift):
    shift = great_shift(shift)
    if direction == "decode":
        shift *= -1
    skip = 0
    for i in range(0, len(text)):
        if text[i] in string.digits and string.punctuation and text[i] != " ":
            skip += 1
        else :
            text[i] = alphabet[i + shift - skip]
    text = ''.join(text)
    print(text)

def great_shift(shift):
    len_alphabet = len(alphabet)
    if shift > len_alphabet:
        shift = shift % len_alphabet
        print(shift)
    # elif shift < (len_alphabet)* -1:        
    #     shift = shift % (len_alphabet - 2)* -1
    #     print(shift)
    return shift
caeser(text, shift)
