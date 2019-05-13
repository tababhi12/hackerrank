from itertools import combinations
string,k = input().split(' ')
if 0 < int(k) <= len(string) and string.isupper():
    for y in range(1,int(k)+1):
        for x in list(combinations(sorted(string),y)):
            print(''.join(x))