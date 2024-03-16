# Task --> Password Generator 
import string
import random

# define the characters that can be used in the password
pass_characters = string.ascii_letters + string.digits + string.punctuation

# ask the user for the desired length of the password
length = int(input("Enter the length of the password: "))
password = ''.join(random.choices(pass_characters, k=length))
print("Your password is:", password)

# ******************Other method *****************
print("\nOther Method to generate random password")
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Shuffle the characters to create randomness
    shuffled_characters = random.sample(characters, len(characters))
    
    # Select a random subset of the shuffled characters
    password = ''.join(random.sample(shuffled_characters, length))
    return password

def main():
    try:
        # Prompt the user for the desired length of the password
        length = int(input("Enter the length of the password: "))
        
        if length <= 0:
            print("Password length must be a positive integer.")
            return
        
        # Generate the password
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()