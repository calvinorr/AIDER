import math

print("Factorial calculator program starting...")

def get_factorial():
    while True:
        user_input = input("Enter a non-negative integer (or 'exit' to quit): ").lower()
        if user_input in ['exit', 'quit']:
            print("Exiting the program. Goodbye!")
            break
        try:
            number = int(user_input)
            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                result = math.factorial(number)
                print(f"The factorial of {number} is: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'exit' to quit.")

if __name__ == "__main__":
    get_factorial()