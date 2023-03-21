class Calculator:
    def add(self, a, b, c=None):
        if c:
            return a + b + c
        return a + b
    
    def subtract(self, a, b, c=None):
        if c:
            return a - b - c
        return a - b
    
    def multiply(self, a, b, c=None):
        if c:
            return a * b * c
        return a * b
    
    def divide(self, a, b, c=None):
        if c:
            return a / b / c
        return a / b
    
    def solve_linear_eq(self, a, b, c):
        if a == 0:
            if b == c:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x = (c - b) / a
            return f"x = {x}"

calc = Calculator()

while True:
    print("Enter the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Solve linear equation")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 6:
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 5:
        num3 = float(input("Enter third number: "))
        print("Result:", calc.solve_linear_eq(num1, num2, num3))
    elif choice in (1, 2, 3, 4):
        try:
            num3 = float(input("Enter third number (optional): "))
        except ValueError:
            num3 = None

        if choice == 1:
            print("Result:", calc.add(num1, num2, num3))
        elif choice == 2:
            print("Result:", calc.subtract(num1, num2, num3))
        elif choice == 3:
            print("Result:", calc.multiply(num1, num2, num3))
        elif choice == 4:
            print("Result:", calc.divide(num1, num2, num3))
        else:
            print("Invalid input")
    else:
        print("Invalid input")
