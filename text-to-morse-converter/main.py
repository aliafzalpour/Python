morse_dic = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
             "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
             "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-","V": "...-", "W": ".--", "X": "-..-",
             "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
             "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": "/"}

dic_to_text = {v: k for k,v in morse_dic.items()}


def text_to_morse(text):
    morse = ""
    for char in text:
        if char in morse_dic:
            morse += morse_dic[char]
            morse += "/"
    print(f"Morse code: {morse}")

def morse_to_text(morse):
    text = ""
    for char in morse.split(" "):
        if char in dic_to_text:
            text += dic_to_text[char]
        elif char == "":
            continue
        else:
            print(f"Warning: Morse code '{char}' not recognized, skipping...")
    print(f"Decoded text: {morse}")


while True:
    translator = input("Please enter encode to morse or decode (e, d, exit): ").lower()
    if translator == "exit":
        print("Goodbye")
        break

    if translator == "encode" or translator == "e":
        input_text = input("Please enter your text: ").upper()
        text_to_morse(input_text)

    elif translator == "decode" or translator == "d":
        input_morse = input("Please enter your morse code: ")
        morse_to_text(input_morse)
