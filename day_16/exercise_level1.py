# Get the current day, month, year, hour, minute and timestamp from datetime module
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# Today is 5 December, 2019. Change this time string to time.
# Calculate the time difference between now and new year.
# Calculate the time difference between 1 January 1970 and now.
# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog

from datetime import datetime,date

date1=datetime.today()
print(date1)

now=datetime.now()
today=date.today()
print(today)

print(today.month)
print(today.day)
print(today.year)



time_one=now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

today = date.today()
new_year=date(year=2027,month=1,day=1)

time_for_newyear=new_year-today
print(time_for_newyear)


then=date(year=1970,month=1,day=1)
time_diff=today-then
print(time_diff)
