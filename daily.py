import time
import datetime
import subprocess

# Define the function to be executed
def my_function():
    print(">>>>>>>>>")
    # Replace this with the actual code you want to execute
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)

# Define the time at which you want the script to run
hour = 16
minute = 32

# Schedule the function to be executed at the specified time every day
while True:
    now = datetime.datetime.now()
    if now.hour == hour and now.minute == minute:
        my_function()
    time.sleep(60)