from numpy import sort
from sqlalchemy import false


names = ["storm","ajoub","mathijs"]

def ask_name():
    name = input("input a name").lower
    if(len(name) == 0):
        names.sort(reverse=True)
        for x in names:
            print(x)
    else:
        names.append(name)
        ask_name()

ask_name()