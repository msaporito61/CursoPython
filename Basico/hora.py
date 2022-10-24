#!/usr/bin/env python3
from urllib.request import urlopen

with urlopen('http://worldtimeapi.org/api/timezone/America/Argentina/Buenos_Aires.txt') as respuesta:
     for linea in respuesta:
        linea = linea.decode()
        if linea.startswith('datetime'):
            print(linea.rstrip())


from datetime import datetime, date, time, timezone

# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)
datetime.combine(d, t)
datetime.datetime(2005, 7, 14, 12, 30)

# Using datetime.now()
datetime.now()   
datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
datetime.now(timezone.utc)   
datetime.datetime(2007, 12, 6, 15, 29, 43, 79060, tzinfo=datetime.timezone.utc)

# Using datetime.strptime()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
dt
datetime.datetime(2006, 11, 21, 16, 30)

# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt:   
     print(it)
