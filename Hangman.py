import random, string, urllib.request


word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
#word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()
selected_word = random.choice(words)
word_slice = list(selected_word)
all_words = list("-" * len(word_slice))
health = len(word_slice)

print(f"someone lif depend on your guess!\nyou have twice health as the correct word that is {health}\ndont lose it!")
print(selected_word)
while word_slice != all_words or health == 0:
    letter = input('Guess a letter: ')
    print(selected_word)
    for i in range(0, len(word_slice)):
        if word_slice[i] == letter:
            all_words[i] = word_slice[i]
    if letter not in selected_word:
        health -= 1

    print(''.join(all_words))
    
    if health == 0:
        print("you kill him!")
        break
    elif health != 0:
        print(f'dead in {health} letters!')