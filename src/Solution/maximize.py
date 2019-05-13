from itertools import product
K,M = list(map(int,input().split(' ')))
list_of_list = []
list_of_count = []
list_main = []

def generate_element(list_main):
    for x in range(len(list_main)):
        yield list_main[x]
if 1<=K<=7 and 1<=M<=1000:
    for x in range(K):
        l1 = list(map(int,input().split(' ')))
        if len(l1[1:]) == l1[0]:
            list_of_list.append(l1[1:])
        else:
            exit(0)
    for y in generate_element(list(product(*list_of_list))):
        list_of_count.append(sum(list(map(lambda x : x ** 2,y))))
    print(max(list(map(lambda x : x % M,list_of_count))))
    