n = int(input())
set_n = set(map(int,input().split()))
b = int(input())
set_b = set(map(int,input().split()))

if 0 < n < 1000 and 0 < b < 1000:
    print(len(set_n.union(set_b)))
