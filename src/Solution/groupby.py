from itertools import groupby
string = input()
if 1 <= abs(int(string)) <= 10000 or string.isdigit():
    for key,grp in groupby(string):
        length = len(list(grp))
        print(f"({length}, {key})",end = ' ')
