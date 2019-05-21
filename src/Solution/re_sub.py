import re

string = ''
for _ in range(int(input())):
    string_1 = input().rstrip()
    if re.findall(r'^(.*?)[\ ]&&[\ ](.*$)',string_1):
        string += ' and '.join(re.findall(r'^(.*?)[\ ]&&[\ ](.*$)[0]',string_1))
    elif re.findall(r'^(.*?)[\ ]\|\|[\ ](.*$)',string_1):
        string += ' or '.join(re.findall(r'^(.*?)[\ ]\|\|[\ ](.*$)[0]',string_1))
    else:
        string += string_1
    string += '\n'
print('-------------------------------------------')
print(string)


import re
N = int(input())

for i in range(N):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or',input()))