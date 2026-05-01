# Password Generator
# Exercise 16 (and Solution)

# Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project. Feel free to skip this and come back when you’re more ready!

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

#    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


"""
This is a great "4-chili" project! Building a password generator is an excellent way to practice working with Python's built-in libraries, handling user input, and managing control flow.
Here is a complete, run-time-ready script that covers all of your requirements, including the "Extra" prompt for choosing password strength.

How This Script Works
• Weak Passwords:
It selects one or two words from a hardcoded list, capitalizes them, and slaps a random two-digit number at the end.
This fulfills the "weak" requirement while mimicking how a lot of real people actually create passwords (e.g., DragonCastle42).

• Strong Passwords:
It forces the inclusion of at least one lowercase letter, one uppercase letter, one digit, and one symbol.
It then fills the remaining requested length with completely random selections from all available characters, and finally shuffles the whole list so the forced characters don't always appear at the beginning.

• The main() Method:
It loops infinitely to let the user generate as many passwords as they want until they explicitly type quit.
"""
# The Python Code
import random
import string

# A predefined list of words for generating "weak" passwords
WORDS = [
    "apple", "river", "mountain", "eagle", "shadow", "forest",
    "ocean", "whisper", "thunder", "cookie", "cactus", "breeze",
    "galaxy", "nebula", "dragon", "knight", "castle", "sword",
    "coffee", "keyboard", "guitar", "rocket", "planet", "comet"
]

def generate_weak_password():
    """Generates a weak password using one or two words and a short number."""
    # Randomly decide to use 1 or 2 words
    # num_words = random.choice()[1, 2]) is a more concise way to randomly choose between 1 and 2, but you could also use random.randint(1, 2) if you prefer.
    num_words = random.choice([1, 2])
    chosen_words = random.sample(WORDS, num_words)

    # Capitalize the words and join them together
    password = "".join(word.capitalize() for word in chosen_words)

    # Add a random 2-digit number at the end
    password += str(random.randint(10, 99))
    return password

def generate_strong_password(length: int = 16):
    """Generates a strong, random password with mixed character types."""
    # Ensure the password is at least 4 characters to fit all constraints
    if length < 4:
        length = 4

    # Define the character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Force at least one character from each category
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length randomly from a combined pool
    all_chars = lower + upper + digits + symbols
    password_chars.extend(random.choices(all_chars, k=length - 4))

    # Shuffle the characters so the forced ones aren't always first
    random.shuffle(password_chars)

    # Join the list into a single string
    return "".join(password_chars)

def main():
    """Main function to run the password generator."""
    print("--- Welcome to the 4-Chili Password Generator! ---")

    while True:
        print("\nOptions: 'weak', 'strong', or 'quit'")
        user_choice = input("How strong do you want your password to be?: ").strip().lower()

        if user_choice == 'quit':
            print("Stay secure! Goodbye.")
            break

        elif user_choice == 'weak':
            weak_pw = generate_weak_password()
            print(f">>> Your weak password is: {weak_pw}")

        elif user_choice == 'strong':
            length_input = input("How long should it be? (Press enter for default 16): ").strip()

            # Handle the user pressing enter vs typing a number
            if length_input == "":
                length = 16
            else:
                try:
                    length = int(length_input)
                except ValueError:
                    print("That wasn't a valid number. Defaulting to 16.")
                    length = 16

            strong_pw = generate_strong_password(length)
            print(f">>> Your strong password is: {strong_pw}")

        else:
            print("Invalid choice. Please type 'weak', 'strong', or 'quit'.")

if __name__ == "__main__":
    main()
