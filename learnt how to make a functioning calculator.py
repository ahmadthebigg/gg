def add(x, y):
  
    return x + y

def subtract(x, y):
    \
    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):
    
    if y == 0:
        return 
    else:
        return x / y

def main():
    
    print("Welcome to my Calculator")
    print("Select operation:")
    print("A. Add")
    print("B. Subtract")
    print("C. Multiply")
    print("D. Divide")

    choice = input("Enter choice (A/B/C/D): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 'A':
        print("Result:", add(num1, num2))
    elif choice == 'B':
        print("Result:", subtract(num1, num2))
    elif choice == 'C':
        print("Result:", multiply(num1, num2))
    elif choice == 'D':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid ")

if __name__ == "__main__":
    main()
