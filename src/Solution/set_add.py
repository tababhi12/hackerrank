N = int(input())
set_ = set()
if 0 < N < 1000:
    for x in range(N):
        s = input()
        set_.add(s)
    print(len(set_))
