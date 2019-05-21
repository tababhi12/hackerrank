import numpy

N,M,P = list(map(int,input().split()))
arrayN = numpy.array([list(map(int,input().split())) for _ in range(N)])
arrayM = numpy.array([list(map(int,input().split())) for _ in range(M)])

print(numpy.concatenate((arrayN,arrayM),axis = 0))
