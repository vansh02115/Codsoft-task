import random
import string


def generate_password():
    print("---- PASSWORD GENERATOR ----")

    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if length <= 0:
        print("Password length must be greater than zero.")
        return

    # Characters used for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ""
    for _ in range(length):
        password += random.choice(characters)

    # Display the generated password
    print("Generated Password:", password)


if __name__ == "__main__":
    generate_password()
