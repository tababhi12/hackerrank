for x in range(int(input())):
    a,set_a,b,set_b = int(input()),set(map(int,input().split())),int(input()),set(map(int,input().split()))
    #print(exec("True' if len(set_a) == len(set_a.intersection(set_b)) else 'False'"))
    print(True if len(set_a) == len(set_a.intersection(set_b)) else False)