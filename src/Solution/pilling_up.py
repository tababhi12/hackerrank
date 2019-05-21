from collections import deque
T = int(input())
list_ = []
all_test = []
global comparing_element
comparing_element = 0
if 1 <= T <= 5:
    for x in range(T):
        n = int(input())
        if 1 <= n <= 100000:
            sidelengths = list(map(int,input().split(' ')))
            length = len(sidelengths)
            if length != n:
                exit()
            elif n == 1:
                print('Yes') 
            else:
                d = deque(sidelengths)
                if d[-1] >= d[0]:
                    global comparing_element
                    comparing_element =  d.pop()
                else:
                    global comparing_element
                    comparing_element =  d.popleft()
                i = 0
                length = len(d)
                while i < length:
                    if d[0] >= d[-1]:
                        global comparing_element
                        if comparing_element >= d[0]:
                            global comparing_element
                            comparing_element =  d.popleft()
                            i = i+1
                        else:
                            print('No')
                            break
                    else:
                        global comparing_element
                        if  comparing_element >= d[-1]:
                            global comparing_element
                            comparing_element =  d.pop()
                            i = i+1
                        else:
                            print('No')
                            break
                if i == n-1:
                    print('Yes')
                



                
 

    # for x in all_test:
    #     d = deque(x)
    #     if len(d) % 2 == 0:
    #         list_ = []
    #         length = len(d) // 2
    #         for x in range(length):
    #             element_1 = d.pop()
    #             element_2 = d.popleft()
    #             if x == length-1:
    #                 if x == 0:
    #                     print('Yes')
    #                 else:
    #                     compare_element = list_[-1]
    #                     if element_1 > compare_element or element_2 > compare_element:
    #                         print('No')
    #                         break
    #                     else:
    #                         if element_1 >= element_2:
    #                             list_.append(element_1)
    #                             list_.append(element_2)
    #                         else:
    #                             list_.append(element_2)
    #                             list_.append(element_1)
    #                         print('Yes')
    #             else:
    #                 if len(list_) == 0:
    #                     if element_1 >= element_2:
    #                         list_.append(element_1)
    #                         list_.append(element_2)
    #                     else:
    #                         list_.append(element_2)
    #                         list_.append(element_1)
    #                 else:
    #                     compare_element = list_[-1]
    #                     if element_1 > compare_element or element_2 > compare_element:
    #                         print('No')
    #                         break
    #                     else:
    #                         if element_1 >= element_2:
    #                             list_.append(element_1)
    #                             list_.append(element_2)
    #                         else:
    #                             list_.append(element_2)
    #                             list_.append(element_1)

    #     else:
    #         if len(d) == 1:
    #             print('Yes')
    #         else:
    #             length = len(d) // 2
    #             list_ = []
    #             for x in range(length+1):
    #                 if x == length:
    #                     element_1 = d.pop()
    #                     compare_element = list_[-1]
    #                     if element_1 > compare_element:
    #                             print('No')
    #                     else:
    #                         print('Yes')
    #                 else:
    #                     element_1 = d.pop()
    #                     element_2 = d.popleft()
    #                     if len(list_) == 0:
    #                         if element_1 >= element_2:
    #                             list_.append(element_1)
    #                             list_.append(element_2)
    #                         else:
    #                             list_.append(element_2)
    #                             list_.append(element_1)
    #                     else:
    #                         compare_element = list_[-1]
    #                         if element_1 > compare_element or element_2 > compare_element:
    #                             print('No')
    #                             break
    #                         else:
    #                             if element_1 >= element_2:
    #                                 list_.append(element_1)
    #                                 list_.append(element_2)
    #                             else:
    #                                 list_.append(element_2)
    #                                 list_.append(element_1)

