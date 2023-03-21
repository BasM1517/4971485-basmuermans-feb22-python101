stack = []

def push(num):
    stack.append(num)

def pop():
    if len(stack) > 0:
        return stack.pop()
    else:
        return None

def add():
    if len(stack) > 1:
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
        return stack[-1]
    else:
        return None

def subtract():
    if len(stack) > 1:
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
        return stack[-1]
    else:
        return None

def multiply():
    if len(stack) > 1:
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
        return stack[-1]
    else:
        return None

def divide():
    if len(stack) > 1:
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
        return stack[-1]
    else:
        return None

# Ask for inputs and perform operations
while True:
    operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
    if operation == 'q':
        break
    elif operation in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        push(num1)
        push(num2)
        if operation == '+':
            result = add()
        elif operation == '-':
            result = subtract()
        elif operation == '*':
            result = multiply()
        elif operation == '/':
            result = divide()
        if result is not None:
            print(f"Result: {result}")
        else:
            print("Error: not enough operands in the stack.")
    else:
        print("Error: invalid operation.")