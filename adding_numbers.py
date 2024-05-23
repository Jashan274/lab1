# A simple Python program 

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main function
def main():
    print("Program to add two numbers")

    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    
    sum_result = add_numbers(num1, num2)

    # Basic Output
    print(f"The sum of {num1} and {num2} is {sum_result}.")


if __name__ == "__main__":
    main()
