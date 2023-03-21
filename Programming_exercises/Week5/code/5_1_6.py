from itertools import count

originalList = [2, 5, 7, 4 , 99, 20, 11, 3 ]

# filter out odd values
evenvalues = [v for v in originalList if v % 2 == 0]

print("Original list:", originalList)
print("List without odd values:", evenvalues)
