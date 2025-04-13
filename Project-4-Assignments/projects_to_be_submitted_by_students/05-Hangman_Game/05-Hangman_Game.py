import random
from lists import WORDS, HANGMAN_PICS

def get_display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    correct_letters = set(word)
    attempts = len(HANGMAN_PICS) - 1
    current_stage = 0

    print("🎮 Welcome to Advanced Hangman!")
    print("-" * 40)

    while attempts > 0:
        print(HANGMAN_PICS[current_stage])
        print(f"\nWord: {get_display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {attempts}\n")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single alphabet.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            print("✅ Good guess!\n")
            if correct_letters.issubset(guessed_letters):
                print(f"🎉 You have guessed '{word}' in {attempts - 6} attempts.")
                print(f"\n🎉 Congratulations! You guessed the word: {word}")
                break
        else:
            print("❌ Wrong guess!")
            current_stage += 1
            attempts -= 1
            print()

    else:
        print(HANGMAN_PICS[-1])
        print(f"\n💀 Game Over! The word was: {word}")

def main():
    while True:
        play_hangman()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing Hangman! Stay sharp.")
            break

if __name__ == "__main__":
    main()
