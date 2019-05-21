# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
for _ in range(int(input())):
    namewithadd = input()
    name,email_id = email.utils.parseaddr(namewithadd)
    if re.match(r'^[a-z][\w_.-]+@[a-z]+\.[a-z]{1,3}$',email_id,flags = re.I):
        print(namewithadd)
    
