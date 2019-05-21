from itertools import combinations
N = int(input())
string = input().split(' ')
K = int(input())
list_of_index = []
if 1 <= N <= 10 and 1<=K<=N:
    comb_ = list(combinations(string,K))
    list_of_element = list(filter(lambda x:'a' in x,comb_))
    print('{0:.10f}'.format(len(list_of_element)/len(comb_)))