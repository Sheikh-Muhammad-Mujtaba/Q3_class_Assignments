import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def countdown_timer(seconds: int):
    """Countdown timer with animated display and colors."""
    try:
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{Fore.YELLOW}{mins:02d}:{secs:02d}{Style.RESET_ALL}"
            print(f"\r⏳ Time Left: {timer}", end="")
            time.sleep(1)
            seconds -= 1
        print(f"\n{Fore.GREEN}✅ Time's up! Great job focusing!")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}⏹ Timer interrupted. Take a break!")

def get_input():
    """Safely get a positive integer input from user."""
    while True:
        try:
            seconds = int(input(Fore.CYAN + f"⏱️  Enter countdown time in seconds: " + Fore.WHITE))
            if seconds > 0:
                return seconds
            print(Fore.RED + "⚠️ Please enter a positive number.")
        except ValueError:
            print(Fore.RED + "❌ Invalid input. Please enter a number.")

def main():
    print(Fore.MAGENTA + "\n==== WELCOME TO COUNTDOWN TIMER ====\n")
    seconds = get_input()
    print(Fore.BLUE + f"\nStarting countdown for {seconds} seconds...\n")
    print(Fore.LIGHTBLACK_EX + "Press Ctrl+C to stop the timer anytime.")
    countdown_timer(seconds)

if __name__ == "__main__":
    main()
