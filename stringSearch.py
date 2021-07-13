"""
Bruteforce string searching algorithm implemented in python.
Following code give the index if substring is present in the target string.

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
        print(i)
        break



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


