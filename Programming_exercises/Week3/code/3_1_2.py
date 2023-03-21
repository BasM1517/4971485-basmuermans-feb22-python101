s = input("Enter a letter: ")
if not s.isalpha():
    print("Please enter only alphabetical characters for your name.")
if(s.isupper()):
    print(s.lower())
else:
    print(s.capitalize())