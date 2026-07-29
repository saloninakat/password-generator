import random
import string
from datetime import datetime


class PasswordGenerator:

    def __init__(self):
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.symbols = string.punctuation


    def generate_password(self, length, use_upper=True,
                          use_lower=True,
                          use_digits=True,
                          use_symbols=True):

        characters = ""

        if use_upper:
            characters += self.uppercase

        if use_lower:
            characters += self.lowercase

        if use_digits:
            characters += self.digits

        if use_symbols:
            characters += self.symbols


        if not characters:
            return "Error: Select at least one character type"


        if length < 6:
            return "Password length should be at least 6 characters"


        password = [
            random.choice(characters)
            for _ in range(length)
        ]

        return "".join(password)



    def password_strength(self, password):

        strength = 0

        if any(char.isupper() for char in password):
            strength += 1

        if any(char.islower() for char in password):
            strength += 1

        if any(char.isdigit() for char in password):
            strength += 1

        if any(char in string.punctuation for char in password):
            strength += 1


        if strength == 4 and len(password) >= 12:
            return "Strong Password"

        elif strength >= 3:
            return "Medium Password"

        else:
            return "Weak Password"



    def save_password(self, password):

        with open("passwords.txt", "a") as file:

            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            file.write(
                f"{time} : {password}\n"
            )

        print("Password saved successfully!")



def main():

    generator = PasswordGenerator()

    print("\n===== Advanced Password Generator =====")

    try:
        length = int(
            input("Enter password length: ")
        )

    except ValueError:
        print("Please enter a valid number")
        return


    upper = input("Include uppercase letters? (y/n): ").lower() == "y"

    lower = input("Include lowercase letters? (y/n): ").lower() == "y"

    digits = input("Include numbers? (y/n): ").lower() == "y"

    symbols = input("Include symbols? (y/n): ").lower() == "y"



    password = generator.generate_password(
        length,
        upper,
        lower,
        digits,
        symbols
    )


    print("\nGenerated Password:")
    print(password)


    print(
        "Strength:",
        generator.password_strength(password)
    )


    save = input(
        "\nDo you want to save password? (y/n): "
    ).lower()


    if save == "y":
        generator.save_password(password)



if __name__ == "__main__":
    main()