import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    print(f"Bisher geraten: {', '.join(sorted(guessed_letters))}\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_failures = len(STAGES) - 1

    print("Willkommen bei Snowman Meltdown!")

    while mistakes < max_failures:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("Glückwunsch! Du hast das Wort erraten und den Schneemann gerettet!")
            return

        guess = input("Rate einen Buchstaben: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Bitte gib einen einzelnen Buchstaben ein.")
            continue

        if guess in guessed_letters:
            print(f"Den Buchstaben '{guess}' hast du schon geraten.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print(f"Falsch! Der Buchstabe '{guess}' ist nicht im Wort. Der Schneemann schmilzt...")
            mistakes += 1
        else:
            print(f"Richtig! '{guess}' ist im Wort enthalten.")

    display_game_state(mistakes, secret_word, guessed_letters)
    print("Oh nein! Der Schneemann ist geschmolzen.")
    print(f"Das geheime Wort war: {secret_word}")
