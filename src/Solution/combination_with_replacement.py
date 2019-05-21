from itertools import combinations_with_replacement
string,k = input().split(' ')
if 0 < int(k) <= len(string) and string.isupper():
    for x in list(combinations_with_replacement(sorted(string),int(k))):
        print(''.join(x))