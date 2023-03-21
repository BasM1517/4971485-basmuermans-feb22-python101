import sys
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
    if int(number) > 0:
        print("this number is positive")
    if int(number) == 0:
        print("0 is neither negative nor positive")
    else :
        print("this number is negative")
    main()
    
main()