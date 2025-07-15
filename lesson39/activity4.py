import datetime

# using now() to get the current date and time
current_datetime = datetime.datetime.now()

print("Time now at greenwich meridian is:", end ="")
print(current_datetime)

# print calendar for the current month
import calendar
print("\n", calendar.calendar(2025))