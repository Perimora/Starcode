import random

WORD_LIST_FILE = "msc/words.txt"


def hangman(vs_cpu: bool):
    """
    Game logic for game 'Hangman'.
    :param vs_cpu: Boolean value to indicate if the word is chosen by the computer.
    """
    if vs_cpu:
        with open(WORD_LIST_FILE, 'r') as f:
            lines = f.readlines()
            word = random.choice(lines).strip()
    else:
        word = "word".upper()

    guesses = set()
    finished = False
    lives = 5

    won = False

    print("Welcome to Hangman!")
    print("Please Enter your name:")

    name = input()

    print(f"Hello, {name}! Nice to meet you!")
    print("Let's play...")

    while not finished:

        print("Enter a guess please: ")

        guess = input().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess only one alphabetical letter!")
            continue

        if guess in word:

            guesses.add(guess)

            print(f"Great! You guessed correctly.")

            letters_left = len(word) - len(set.intersection(set(word), guesses))

            if letters_left:
                print(f"{letters_left} letters left until you have won!")
            else:
                won = True
                finished = True

        else:
            lives -= 1
            print("Wrong guess, you lost a live!")
            print(f"You have {lives} lives remaining.")
            if lives == 0:
                print("Oh no, you lost the game!")
                finished = True

    if won:
        print("You won!")
    else:
        print("You lost!")


if __name__ == "__main__":
    hangman()
