m,n = list(map(int,input().split()))
if 1 <= n <=100000 and 1 <= m <=100000:
    array = set(map(int,input().split()))
    if len(array) == m:
        A = set(map(int,input().split()))
        B = set(map(int,input().split()))
        if len(A) == n and len(A) == n:
            print(len(array.intersection(A))-len(array.intersection(B)))