M = int(input())
M_value = set(map(int,input().split(' ')))
N = int(input())
N_value = set(map(int,input().split(' ')))
list_ = []
list_.extend(M_value.difference(N_value))
list_.extend(N_value.difference(M_value))
for x in sorted(list_):
    print(x)