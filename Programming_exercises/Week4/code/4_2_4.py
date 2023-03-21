length = int(input("how many characters should you're triangle be"))
def triangle(length):
    for x in range(length):
        spaces = length - x
        print(" "*spaces + "*"*x)
triangle(length)
