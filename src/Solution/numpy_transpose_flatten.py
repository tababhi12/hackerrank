import numpy

N,M = list(map(int,input().split()))
main_list = []
for _ in range(N):
    main_list.append(list(map(int,input().split())))

array = numpy.array(main_list)
print(numpy.transpose(array))
print(array.flatten())



