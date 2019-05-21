import re
def fun(s):
    # return True if s is a valid email, else return False
    list_ = re.split('; |, |\@|\.', s)
    if len(list_) == 3:
        if len(list(filter(lambda x: x.isalnum() or x in ['-','_'] , list_[0]))) == len(list_[0]):
            if len(list(filter(lambda x: x.isalnum() , list_[1]))) == len(list_[1]):
                if len(list_[2]) <= 3:
                    return True
                else:
                    False
            else:
                return False
        else:
            return False
    else:
        return False
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)