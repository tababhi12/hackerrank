# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
set_n = set(map(int,input().split()))
b = int(input())
for x in range(b):
    print(x)
    command,value = input().split()
    value = int(value)
    set_b = set(map(int,input().split()))
    if 0 < len(set_n) < 1000 and 0 < len(set_b) < 100 and 0 < b < 100 and len(set_b) == value:
        print(command,value)
        if command == 'intersection_update':
            set_n.intersection_update(set_b)
            print(set_n)
        if command == 'update':
            set_n.update(set_b)
            print(set_n)
        if command == 'symmetric_difference_update':
            set_n.symmetric_difference_update(set_b)
            print(set_n)
        if command == 'difference_update':
            set_n.difference_update(set_b)
            print(set_n)
print(sum(set_n))

#Second soluution
m, base_set = input(), set(map(int, input().split()))
for i in range(0,int(input())):
    exec("base_set.{0}({1})".format(input().split()[0], set(map(int, input().split())) ))
print(sum(base_set))
