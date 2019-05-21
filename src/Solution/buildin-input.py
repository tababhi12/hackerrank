x,k = list(map(int,input().split()))
poly = input()
print(True if eval(poly.replace('x',str(x))) == k else False)