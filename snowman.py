from game_logic import play_game


def main():
    while True:
        play_game()

        play_again = input("\nMöchtest du noch einmal spielen? (ja/nein): ").lower()
        if not play_again.startswith("j"):
            break

    print("\nDanke fürs Spielen! Auf Wiedersehen!")


if __name__ == "__main__":
    main()