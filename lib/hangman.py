"""
TODO:
    - target input (eigener input + word list für spiel)
"""


def hangman():
    word = "word".upper()
    letters_guessed = 0
    guesses = []
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

        if len(guess) or not guess.isalpha():
            print("Please guess only one letter!")
            continue

        if guess in word:

            guesses.append(guess)

            print(f"Great! You guessed correctly.")

            count = 0

            for letter in word:
                if letter in guesses:
                    count += 1

                else:
                    continue

            if count == len(word):
                finished = True
                won = True

        else:
            print("Wrong guess, you lost a live!")
            print(f"You have {lives} lives remaining.")

            lives -= 1
            if lives == 0:
                finished = True

    if won:
        print("You won!")
    else:
        print("You lost!")


if __name__ == "__main__":
    hangman()
