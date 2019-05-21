import re
times = int(input())
for _ in range(times):
    number = input()
    if len(number) == 10 and number.isdigit() and re.match(r'^[789](\d+)',number):
        print('YES')
    else:
        print('NO')