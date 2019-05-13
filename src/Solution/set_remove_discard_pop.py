n = int(input())
if 0 < n < 20:
    s = set(map(int,input().split()))
    N = int(input())
    if 0 < N < 20:
        for x in range(N):
            list_ = input().split()
            if len(list_) == 1:
                try:
                    s.pop()
                except:
                    pass
            else:
                command,value = list_[0],int(list_[1])
                if command == 'remove':
                    try:
                        s.remove(value)
                    except:
                        pass
                if command == 'discard':
                    s.discard(value)

    print(sum(s))