def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Welcome to the Factorial Calculator!")
    try:
        number = int(input("Enter a non-negative integer to calculate its factorial: "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            result = factorial(number)
            print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()