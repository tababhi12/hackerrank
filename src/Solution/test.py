from itertools import product
K,M = list(map(int,input().split(' ')))
list_of_list = []
list_of_count = []
list_main = []

def generate_element(list_main):
    for x in len(list_main):
        yield list_main[x]
if 1<=K<=7 and 1<=M<=1000:
    for x in range(K):
        l1 = list(map(int,input().split(' ')))
        if len(l1[1:]) == l1[0]:
            list_of_list.append(l1[1:])
        else:
            exit(0)
    print(list_of_list)
    for y in generate_element(list(itertools.product(*l2))):
        list_of_count.append(sum(list(map(lambda x : x ** 2,y))))
    print(max(list_of_count))
    # try:   
    #     for x in range(len(list_of_list)-1):
    #         print(x)
    #         for y in list_of_list[x]:
    #             print(y)
    #             for z in list_of_list[x+1]:
    #                 list_ = []
    #                 list_.append(y)
    #                 list_.append(z)
    #                 list_main.append(list_)
    # except Exception as e:
    #     print(e)
    print(list_main)
    # for x in list_of_list:
    #     list_of_count.append(max(x))
    # print(list_of_count)
    # print(sum(list(map(lambda x :x * x,list_of_count))))
    #print(max(list_of_count)%1000)
    
