N = int(input())
set_ = {}
if 0 < N < 1000:
    for x in range(N):
        set_.add(x)
    print(len(set_))
