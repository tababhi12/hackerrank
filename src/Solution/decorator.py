import re
def wrapper(f):
    def fun(l):
        # complete the function
        f(['+91 '+c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 




#second

l1 = ['07895462130', '919875641230', '9195969878']
l2 = []
for x in l1:
    if len(x) == 10:
        l2.append('+91 '+x[0:6] + ' ' + x[5:])
        
    elif re.findall('(?<=91)(.*?)$',x):
        number = re.findall('(?<=91)(.*?)$',x)[0]
        print(x,number)
        l2.append('+91 '+number[0:6] + ' ' + number[5:])
        
    elif re.findall('(?<=\+91)(.*?)$',x):
        number = re.findall('(?<=\+91)(.*?)$',x)
        print(x,number)
        l2.append('+91 '+number[0:6] + ' ' + number[5:])
        
    elif re.findall('(?<=0)(.*?)$',x):
        number = re.findall('(?<=0)(.*?)$',x)[0]
        print(x,number)
        l2.append('+91 '+number[0:6] + ' ' + number[5:])
    
    else:
        pass
print(*sorted(l2))