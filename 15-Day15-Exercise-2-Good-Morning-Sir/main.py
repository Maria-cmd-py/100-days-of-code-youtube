import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

Or
from datetime import datetime  # Import the datetime module

# Get the current time
current_time = datetime.now()  # Get the current date and time

# Extract the hour from the current time
current_hour = current_time.hour  # Get the current hour (0-23)

# Determine the appropriate greeting
if current_hour < 12:  # If the hour is less than 12, it's morning
    print("Good Morning, Sir!")
elif current_hour < 18:  # If the hour is less than 18 (but 12 or more), it's afternoon
    print("Good Afternoon, Sir!")
else:  # Otherwise, it's evening or night
    print("Good Night, Sir!")

OR

time=int(input("Enter rhe num:"))
if(time<12):
  print("Good Morning Sir")
elif(time<17):
  print("Good Afternoon Sir")
else:
  print("Good Evening Sir")
