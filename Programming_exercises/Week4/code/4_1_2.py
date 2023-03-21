stack = []

def push(value):
    stack.append(value)

def pop():
    if len(stack) == 0:
        print("Stack is empty")
        return None
    else:
        return stack.pop()

def calculate(op, num_values):
    if op == '+':
        if num_values == 2:
            b = pop()
            a = pop()
            push(a + b)
        elif num_values == 3:
            c = pop()
            b = pop()
            a = pop()
            push(a + b + c)
    elif op == '-':
        if num_values == 2:
            b = pop()
            a = pop()
            push(a - b)
        elif num_values == 3:
            c = pop()
            b = pop()
            a = pop()
            push(a - b - c)
    elif op == '*':
        if num_values == 2:
            b = pop()
            a = pop()
            push(a * b)
        elif num_values == 3:
            c = pop()
            b = pop()
            a = pop()
            push(a * b * c)
    elif op == '/':
        if num_values == 2:
            b = pop()
            a = pop()
            push(a / b)
        elif num_values == 3:
            c = pop()
            b = pop()
            a = pop()
            push(a / b / c)
    elif op == '**':
        if num_values == 2:
            b = pop()
            a = pop()
            push(a ** b)
        elif num_values == 3:
            c = pop()
            b = pop()
            a = pop()
            push(a ** (b ** c))
    else:
        print("Invalid operator")

num_values = input("Enter number of values (2 or 3): ")
if num_values == '2' or num_values == '3':
    while True:
        num_str = input("Enter space-separated numbers to push onto stack: ")
        nums = num_str.split()
        if len(nums) == int(num_values):
            for num in nums:
                push(float(num))
            break
        else:
            print(f"Please enter {num_values} numbers")

    while True:
        print("Enter an operator (+, -, *, /, **):")
        operator = input().strip()

        if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '**':
            if len(stack) < int(num_values):
                print("Not enough values in the stack")
            else:
                calculate(operator, int(num_values))
                print("Result: ", stack[-1])
        else:
            print("Invalid operator")
else:
    print("Invalid input")
