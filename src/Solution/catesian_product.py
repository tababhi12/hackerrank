from itertools import product
A = input().split(' ')
B = input().split(' ')
list_ =list(product(A,B))
for x in list_:
    print(tuple(map(int,x)),end =' ')