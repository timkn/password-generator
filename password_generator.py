import secrets
import string

# all characters for the password
chars = string.digits + string.ascii_letters + string.punctuation


# ask the user how many characters the password should have
def get_character_count():
    count: str = input("How many characters should the password have: ")
    try:
        return int(count)
    except ValueError:
        print("The input must be a number.")
        get_character_count()


if __name__ == '__main__':
    print("- Password Generator by tym21 -\n")
    length = get_character_count()
    print("".join(secrets.choice(chars) for _ in range(length)))
