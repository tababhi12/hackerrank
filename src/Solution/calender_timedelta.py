from datetime import timedelta
import dateutil.parser
import pytz
for x in range(int(input())):
    date1,date2 = input(),input()
    date_orig1 = dateutil.parser.parse(date1)
    date_utc1 = date_orig1.astimezone(pytz.UTC)

    date_orig2 = dateutil.parser.parse(date2)
    date_utc2 = date_orig2.astimezone(pytz.UTC)

    diff = date_utc1 - date_utc2
    print(int(abs(diff.total_seconds())))

    from datetime import datetime as dt

    #second solution
    fmt = '%a %d %b %Y %H:%M:%S %z'
    print(int(abs((dt.strptime(date1, fmt) - 
                   dt.strptime(date2, fmt)).total_seconds())))