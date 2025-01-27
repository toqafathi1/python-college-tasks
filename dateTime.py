
import datetime

# creating a date
# d = datetime.date(2023, 9, 14)
# print(d)

# date today
# today = datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# # weekday
# print(today.weekday)  # monday 0 sunday 6
# print(today.isoweekday)  # Monday 1 sunday 7

# tdelta = datetime.timedelta(days=7)
# print(today + tdelta)  # print what the date gona be after 7 days
# print(today - tdelta)  # print what the date gona be before 7 days

# calculate how mant days left until my birthday
# bday = datetime.date(2023, 10, 16)
# till_day = bday - today
# print(till_day.days)

# t = datetime.time(9, 30, 45, 10000)
# print(t)

# td = datetime.datetime(2023, 9, 14, 1, 9, 20, 10000)
# print(td.date())  # td.time()

# td_now = datetime.datetime.now()
# print(td_now)

# pytz
import pytz

# dt = datetime.datetime(2023, 9, 14, 1, 9, 20, 10000, tzinfo=pytz.utc)
# print(dt)

dt_now = datetime.datetime.now(tz=pytz.utc)
# print(dt_now)

for tz in pytz.all_timezones:
    print(tz)
dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
