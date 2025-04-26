import random
from typing import Optional

LETTERS: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS: str = "0123456789"
SYMBOLS: str = "!@#$%^&*()_+-=[]{}|;:,.<>?/"


def get_password_length(choice: str) -> int:

    predefined_lengths: dict[str, int] = {"1": 8, "2": 12, "3": 16}

    if choice in predefined_lengths:
        return predefined_lengths[choice]
    elif choice == "4":

        try:
            custom_length: int = int(
                input("Enter the desired length of your password: "))

            if custom_length <= 0:
                raise ValueError
            return custom_length

        except ValueError:
            print("Invalid input. Defaulting to medium length (12 characters).")
            return 12

    else:
        print("Invalid choice. Defaulting to medium length (12 characters).")
        return 12


def get_character_pool(include_letters: bool, include_numbers: bool, include_symbols: bool) -> str:

    if not (include_letters and include_numbers and include_symbols):
        print("You must include at least one character type. Defaulting to letters.")
        return LETTERS

    pool: str = ""
    if include_letters:
        pool += LETTERS
    if include_numbers:
        pool += NUMBERS
    if include_symbols:
        pool += SYMBOLS
    return pool


def generate_password(length: int, pool: str) -> Optional[str]:

    if length > len(pool):
        print(
            "Warning: Password length exceeds the pool size. Allowing character repetition.")
        return "".join(random.choices(pool, k=length))
    return "".join(random.sample(pool, k=length))


def main() -> None:

    print("\nWelcome to the Password Generator!")
    print("=" * 40)
    print("Select the length of your password:")
    print("1. Short (8 characters)")
    print("2. Medium (12 characters)")
    print("3. Long (16 characters)")
    print("4. Custom length")

    choice: str = input("Enter your choice (1-4): ")
    password_length: int = get_password_length(choice)

    include_letters: bool = input(
        "\nInclude letters? default(y): ").strip().lower() in ["y", ""]
    include_numbers: bool = input(
        "Include numbers? default(y): ").strip().lower() in ["y", ""]
    include_symbols: bool = input(
        "Include symbols? default(y): ").strip().lower() in ["y", ""]

    pool: str = get_character_pool(
        include_letters, include_numbers, include_symbols)
    password: Optional[str] = generate_password(password_length, pool)

    if password:
        print(f"\nYour generated password is: {password}")
        print("Password length:", password_length)


if __name__ == "__main__":
    main()
