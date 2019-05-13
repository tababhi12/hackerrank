# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n,m = list(map(int,input().split()))
base_list,set_A,set_B = list(map(int,input().split())),set(map(int,input().split())),set(map(int,input().split()))
counter_base = dict(Counter(base_list))
i = 0
base_set = set(base_list)
for x_a in set_A.intersection(base_set):
    i = i + counter_base[x_a]
for x_b in set_B.intersection(base_set):
    i = i - counter_base[x_b]

print(i)