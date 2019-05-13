from collections import Counter
k,base_set = int(input()),list(map(int,input().split()))
print(list(Counter(base_set))[list(dict(Counter(base_set)).values()).index(1)])