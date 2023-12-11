import random
words = ['Salad','Sandwich','Bread','Steak','Fish','shrimp','Rice','Spaghetti','pizza','hamburger','Eggs','Cheese','sausages','Milk','Candy',
         'Cookie','Pie','Cake','Cupcake','noodles','chicken','beef','salt','sugar','pepper','mutton']
def random_word():
    word = random.choice(words)
    return word.upper()
def play(word):
    word_c = '_'*len(word)
    guessed = False
    guessed_letter = []
    guessed_words = []
    incorrect_attempt = 0
    tries = 6
    print("Let's play the Hangman game.")
    print("Guess the ",len(word)," letter food item.")
    print(display_hang(tries))
    print(word_c)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess the Food Item: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess is guessed_letter:
                print('Already guessed',guess)
            elif guess not in word:
                incorrect_attempt +=1
                tries -=1
                guessed_letter.append(guess)
                print("Incorrect guess ", guess)
                if incorrect_attempt >=2 and incorrect_attempt % 2 == 0:
                    l = input("Do you want a hint(y/n) :").upper()
                    if l == 'Y':
                        hint = random.choice([letter for letter in word if letter not in guessed_letter ])
                        print(f"Hint : The word contains the letter '{hint}'.")
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


