import random
words = ['soup','mount','extend','brown','expert','tired','humidity','backpack','crust','dent','market','knock','smite','windy','coin','throw',
    'silence','bluff','downfall','climb','lying','weaver','kickoff','match','foreman','excite','thinking','mend','allergen','pruning','coat','emerald',
    'manic','multiple','square','funded','funnel','sailing','dream','mutation','strict','mystic','film','guide','strain','settle','emigrate','marching',
    'optimal','medley','endanger','rage','figure','plague','aloof','there','reusable','refinery','suffer']

def random_word():
    word = random.choice(words)
    return word.upper()
def play(word):
    word_c = '_'*len(word)
    guessed = False
    guessed_letter = []
    guessed_words = []
    tries = 6
    print("Let's play the Hangman game.")
    print(display_hang(tries))
    print(word_c)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess the word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess is guessed_letter:
                print('Already guessed',guess)
            elif guess not in word:
                tries -=1
                guessed_letter.append(guess)
            else:
                print("good guess",guess)
                guessed_letter.append(guess)
                word_as_list = list(word_c)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for ind in indices:
                    word_as_list[ind] = guess
                word_c = "".join(word_as_list)
                if "_" not in word_c:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_c = word
        else:
            print("Not a valid guess.")
        print(display_hang(tries))
        print(word_c)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ".")




def display_hang(tries):
    hang = ['''
H A N G M A N
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
=========
''','''
H A N G M A N
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
=========
''','''
H A N G M A N
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
=========
''','''
H A N G M A N
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========
''','''
H A N G M A N
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
''','''
H A N G M A N
    +---+
    |   |
    O   |
        |
        |
        |
=========
''','''
H A N G M A N
    +---+
    |   |
        |
        |
        |
        |
=========
'''
]
    return hang[tries]

def main():
    word = random_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = random_word()
        play(word)

if __name__ == "__main__":
    main()


