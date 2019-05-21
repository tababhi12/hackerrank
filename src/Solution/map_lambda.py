cube = lambda x: x ** 3


def fibonacci(n):
    if n > 2:
        list_ = [0,1]
        for _ in range(n-2):
            list_.append(list_[-1] + list_[-2])
        return list_
    else:
        if n == 1:
            return [0]
        elif n == 2:
            return [0,1] 
        else:
            return []

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))