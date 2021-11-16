from datetime import date,datetime
import time 
from dateutil.relativedelta import relativedelta

def get_dates(b, e, s ,f):
    start = date.fromisoformat(b)
    end = date.fromisoformat(e)
    date_rage = []
    unix_range = []
    while True:
        next_start = start + relativedelta(days=s)
        this_end = next_start - relativedelta(days=1)
        if end <= this_end:
            startt = datetime.strptime(start.strftime('%Y%m%d'), '%Y%m%d').replace(hour=0, minute=0, second=1)
            endt = datetime.strptime(end.strftime('%Y%m%d'), '%Y%m%d').replace(hour=23, minute=59, second=59)
            date_rage.append((startt,endt))
            st = time.mktime(startt.timetuple())
            en = time.mktime(endt.timetuple())
            unix_range.append((int(st),int(en)))
            break
        startt = datetime.strptime(start.strftime('%Y%m%d'), '%Y%m%d').replace(hour=0, minute=0, second=1)
        endt = datetime.strptime(this_end.strftime('%Y%m%d'), '%Y%m%d').replace(hour=23, minute=59, second=59)
        date_rage.append((startt,endt))
        st = time.mktime(startt.timetuple())
        en = time.mktime(endt.timetuple())
        unix_range.append((int(st),int(en)))
        start = next_start
    if f == 'unix':
        return unix_range
    else:
        return date_rage

begin = '2021-05-01'
end = '2021-11-22'
step = 15
format = 'unix'
tt = get_dates(begin,end,step,format)
print(tt)