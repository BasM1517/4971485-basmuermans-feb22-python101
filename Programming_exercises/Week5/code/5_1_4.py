from tracemalloc import stop
from requests import delete

from sqlalchemy import false


numbers = [1,2,2,2,3,1,4,2,3,6,7,9,7,3]

def deletedoubles():
    new_numbers = list(set(numbers))

    print(new_numbers)
deletedoubles()

