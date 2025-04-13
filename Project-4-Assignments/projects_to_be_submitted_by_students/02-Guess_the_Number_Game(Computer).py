import random

def computer_guess(x):
    
    print(f"\nThink of a number between 1 and {x}. I'll try to guess it!")
    print("Enter 'H' if my guess is too high, 'L' if too low, or 'C' if correct.\n")
    
    low = 1
    high = x
    attempts = 0
    feedback = ''
    previous_guesses = set()
    
    while feedback != 'c':
        
        if low > high:
            print("Wait a minute... You must have changed your number! Let's start over.")
            low = 1
            high = x
            attempts = 0
            previous_guesses.clear()
        
        while True:
            guess = random.randint(low, high)
            if guess not in previous_guesses:
                break
            if low == high:  
                print("I've guessed all possible numbers. Did you make a mistake?")
                return
        
        previous_guesses.add(guess)
        attempts += 1
        
        feedback = input(f"Attempt #{attempts}: Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        while feedback not in ['h', 'l', 'c']:
            feedback = input("Please enter H, L, or C: ").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"\n🎉 Yay! I guessed your number {guess} correctly in {attempts} attempts!")

MAX_NUMBER = 100  

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print(f"I'll try to guess your number between 1 and {MAX_NUMBER}.")
    
    while True:
        computer_guess(MAX_NUMBER)
        
        play_again = input("\nWould you like to play again? (Y/N): ").lower()
        while play_again not in ['y', 'n']:
            play_again = input("Please enter Y or N: ").lower()
        
        if play_again == 'n':
            print("\nThanks for playing! Goodbye!")
            break