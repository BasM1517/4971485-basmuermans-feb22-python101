import sys
number = input("Fill in a number thats either negative or positive ")
try:
    int(number)
except ValueError:
    try:
        float(number)
    except ValueError:
        print("This is not a number")
        sys.exit()
if number > 0:
    print("this number is positive")
else :
    print("this number is negative")