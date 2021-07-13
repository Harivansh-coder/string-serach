"""
Bruteforce string searching algorithm implemented in python.
Following code give the index from it starts.

Has a time complexity of O(mxn).
m = length of target string
n = length of the pattern to be searched

"""
mainString = input("Enter the main string: ")
m = len(mainString)
patt = input("Enter the substring: ")
p = len(patt)

i = 0

for i in range(m - p + 1):
    j = i
    k = 0
    while k < p and mainString[j] == patt[k]:

        k += 1
        j += 1

    if k == p:
        break


print(i)

"""
# OUTPUT

    Enter the main string: python
    Enter the substring: thon
    2

# OUTPUT

    Enter the main string: sorting algorithm
    Enter the substring: algo
    8

"""


