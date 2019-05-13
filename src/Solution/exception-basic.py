
for x in range(int(input())):
    try:
        l_ = list(map(int,input().split()))
        print(l_[0] // l_[1])
    except ZeroDivisionError as e:
        print(f"Error Code:{e}")
    except ValueError as e:
        print(f"Error Code:{e}")