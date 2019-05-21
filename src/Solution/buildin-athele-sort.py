n,m = list(map(int,input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())
zippped_data = list(zip(*arr))
result = sorted(dict(enumerate(zippped_data[k])).items(), key = 
             lambda kv:(kv[1], kv[0]))
for x in result:
    print(' '.join(list(map(str,arr[x[0]]))))
