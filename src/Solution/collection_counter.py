from collections import Counter
list_main = []
X = int(input())
total_cost = 0
if 0 < X < 1000:
    element_list = list(map(int,input().split(' ')))
    if len(element_list) == X:
        N = int(input())
        if 0 < N < 1000:
            for n in range(N):
                list_ = list(map(int,input().split(' ')))
                if 2 < list_[0] < 20 and 20 < list_[1] < 100:
                    if list_[0] in element_list:
                        print(element_list)
                        print(list_)
                        total_cost = total_cost + list_[1]
                        element_list.remove(list_[0])
                        print(total_cost)