# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    line = input()
    words = re.findall(r'[\w: ]#[a-f0-9]+[;,)]',line,flags = re.I)
    for word in words:
        print(word.strip().replace(';','').replace(':','').replace(')','').replace(',',''))
