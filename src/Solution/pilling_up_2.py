from collections import deque
import os

def check_pilling(list_):
    d = deque(list_)
    n = len(list_)
    if d[-1] >= d[0]:
        list_.append(d.pop())
    else:
        list_.append(d.popleft())
    i = 0
    length = len(d)
    while i < length:
        if d[0] >= d[-1]:
            if list_[-1] >= d[0]:
                list_.append(d.popleft())
                i = i+1
            else:
                print('No')
                break
        else:
            if list_[-1] >= d[-1]:
                list_.append(d.pop())
                i = i+1
            else:
                print('No')
                break
    if i == n-1:
        print('Yes')
        
                                    
def generate_element():
    file = os.getcwd() + '\src\Solution\\input_pilling.txt'
    with open(file,'r') as r:
        lines = r.readlines()
        print(len(lines[4].split()))
        check_pilling(lines[4].split())
generate_element()