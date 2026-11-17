import datetime
from bday_messages import random_message

today = datetime.date(2026,11,17)

next_birthday = datetime.date(2026,12,22)

days_away = next_birthday - today

if today == next_birthday:
    print(random_message)
else:
    print(f"My next birthday is {days_away} days away!")