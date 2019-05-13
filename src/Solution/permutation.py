from itertools import permutations
A = input().split(' ')
if len(A) == 1:
    string = A[0]
    k = len(A[0])
else:
    string,k = A
for x in list(permutations(sorted(string),int(k))):
    print(''.join(x))