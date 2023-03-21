import sys

numbers = []

def main():
    number = input("Fill in a number thats either negative or positive press q to exit ")
    if number == "q":
        sys.exit()
    try:
        int(number)
    except ValueError:
        try:
            float(number)

        except ValueError:
            print("This is not a number")
            main()
    if number == 0:
        print("hello")
        print(numbers)
        print(sum(numbers))
    else:
        numbers.append(number)
    main()
    
main()