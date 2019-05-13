def pilling_up(list_):
    compare_ele = 0
    if list_[0] >= list_[-1]:
        compare_ele = list_[0]
        del list_[0]
    else:
        compare_ele = list_[-1]
        del list_[-1]
    while len(list_) != 0:
        if list_[0] > compare_ele or list_[-1] > compare_ele:
            return 'No'
        else:
            if list_[0] >= list_[-1]:
                compare_ele = list_[0]
                del list_[0]
            else:
                compare_ele = list_[-1]
                del list_[-1]
    else:
        return 'Yes'
        
for x in range(int(input())):
    n,base_list = int(input()),list(map(int,input().split()))
    print(pilling_up(base_list))