import re
S,k = input(),input()
count = 0
for x in range(len(S)):
    if k[0] == S[x]:
        if k == S[x:x+len(k)]:
            print(f'({x}, {x+len(k)-1})')
            count = count + 1

if count == 0:
    print(f'({-1}, {-1})')
    