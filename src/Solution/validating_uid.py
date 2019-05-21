# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
for _ in range(int(input())):
    uuid = input()
    if uuid.isalnum() and len(uuid) == 10 and len(uuid) == len(set(uuid)) and len(re.findall(r'[0-9]',uuid)) > 2 and len(re.findall(r'[A-Z]',uuid)) > 1:
        print('Valid')
    else:
        print('Invalid')
