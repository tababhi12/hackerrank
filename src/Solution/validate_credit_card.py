import re
from itertools import groupby
for _ in range(int(input())):
    credit_card = input()
    if re.match(r'^[456][0-9]{3}(-){0,1}[0-9]{4}(-){0,1}[0-9]{4}(-){0,1}[0-9]{4}$',credit_card) and max([len(list(grp)) for key,grp in groupby(credit_card.replace('-',''))]) < 4:
        print('Valid')
    else:
        print('Invalid')