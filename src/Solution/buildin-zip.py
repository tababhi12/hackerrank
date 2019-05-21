N,X = list(map(int,input().split()))
l1 = []
for x in range(X):
    l1.append(list(map(float,input().split())))
l2 = [print(sum(y) / X) for y in list(zip(*l1))]

