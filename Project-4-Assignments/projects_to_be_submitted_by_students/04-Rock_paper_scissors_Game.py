import random
from colorama import init, Fore, Style
from typing import Set, Tuple, Dict

# Initialize colorama
init(autoreset=True)

CHOICES: Dict = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

def display_welcome():
    """Display colorful welcome message and instructions"""
    print(Fore.CYAN + """
    *********************************************
    *                                           *
    *      """ + Fore.YELLOW + "ROCK-PAPER-SCISSORS GAME" + Fore.CYAN + """      *
    *                                           *
    *********************************************
    """)
    print(Fore.GREEN + "Rules:")
    print(Fore.MAGENTA + "- Rock crushes Scissors")
    print(Fore.MAGENTA + "- Scissors cuts Paper")
    print(Fore.MAGENTA + "- Paper covers Rock")
    print(Fore.MAGENTA + "- Same choice is a tie")
    print(Fore.CYAN + "\nYou'll play multiple rounds against the computer.")
    print(Fore.CYAN + "Let's see who wins the most rounds!\n")

def get_rounds():
    """Get and validate number of rounds"""
    while True:
        try:
            rounds: int = int(input(Fore.YELLOW + "How many rounds would you like to play? (1-10): " + Fore.WHITE))
            if 1 <= rounds <= 10:
                return rounds
            else:
                print(Fore.RED + "Please enter a number between 1 and 10.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 10.")

def get_user_choice():
    """Get and validate user choice"""
    while True:
        user: str = input(Fore.YELLOW + "\nWhat's your choice? \n'r' for rock, 'p' for paper, 's' for scissors: " + Fore.WHITE).lower()
        if user in CHOICES:
            return user
        print(Fore.RED + "Invalid input. Please enter 'r', 'p', or 's'.")

def display_choices(user, computer):
    """Display the choices with colorful formatting"""
    color_map: Dict = {
        'r': Fore.BLUE,
        'p': Fore.GREEN,
        's': Fore.MAGENTA
    }
    print(f"\n{Fore.YELLOW}You chose: {color_map[user]}{CHOICES[user]}{Style.RESET_ALL}")
    print(f"{Fore.RED}Computer chose: {color_map[computer]}{CHOICES[computer]}{Style.RESET_ALL}")

def is_win(player, opponent):
    """Determine if player wins against opponent"""
    return (player == 'r' and opponent == 's') or \
           (player == 'p' and opponent == 'r') or \
           (player == 's' and opponent == 'p')

def determine_winner(user, computer):
    """Determine the winner of a round"""
    if user == computer:
        return "tie"
    elif is_win(user, computer):
        return "user"
    else:
        return "computer"

def play():
    """Main game function"""
    display_welcome()
    rounds: int = get_rounds()
    user_point: int = 0
    com_point: int = 0

    for current_round in range(1, rounds + 1):
        print(Fore.CYAN + f"\n=== Round {current_round} of {rounds} ===")

        user: str = get_user_choice()
        computer: str = random.choice(['r', 'p', 's'])

        display_choices(user, computer)
        result: str = determine_winner(user, computer)

        if result == "tie":
            print(Fore.CYAN + "It's a tie!")
        elif result == "user":
            print(Fore.GREEN + "You won this round!")
            user_point += 1
        else:
            print(Fore.RED + "You lost this round!")
            com_point += 1

        print(Fore.YELLOW + f"\nCurrent Score: {user_point} - You | {com_point} - Computer")

    # Final results
    print(Fore.CYAN + "\n=== Final Results ===")
    print(Fore.YELLOW + f"You won {user_point} out of {rounds} rounds!")

    if user_point > com_point:
        print(Fore.GREEN + "🎉 Congratulations! You're the overall winner!")
    elif user_point == com_point:
        print(Fore.CYAN + "🤝 It's a draw! Good game!")
    else:
        print(Fore.RED + "💻 Computer wins overall. Better luck next time!")

    print(Fore.MAGENTA + "\nThanks for playing!")

if __name__ == "__main__":
    play()
