base_set = set(map(int,input().split()))
list_ = []
for x in range(int(input())):
    set_N = set(map(int,input().split()))
    if len(set_N.difference(base_set)) == 0:
        list_.append('True')
    else:
        list_.append('False') 
if 'False' in list_:
    print('False')
else:
    print('True')
 
    