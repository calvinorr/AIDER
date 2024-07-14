import random
import string

def generate_password(length=12):
     """Generate a random password of the specified length."""
     characters = string.ascii_letters + string.digits + string.punctuation
     password = ''.join(random.choice(characters) for _ in range(length))
     return password

def main():
     print("Welcome to the Random Password Generator!")
     while True:
         try:
             length = int(input("Enter the desired password length (or 0 to quit): "))
             if length == 0:
                 print("Thank you for using the Random Password Generator. Goodbye!")
                 break
             elif length < 4:
                 print("Password length must be at least 4 characters.")
             else:
                 password = generate_password(length)
                 print(f"Your generated password is: {password}")
         except ValueError:
             print("Please enter a valid number.")

if __name__ == "__main__":
     main()