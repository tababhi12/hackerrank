# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby
s = input()
a = 0
for key,grp in groupby(s):
    length = len(list(grp))
    print(key,length)
    if length > a:
        if key.isalnum():
            a = length
            element = key
if a == 1:
    print('-1')
else:
    print(element)