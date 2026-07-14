# Python_Timer
It's a timer program written in Python.

I modified the code originally scripted by Bro Code. I added an option to separately enter hours and minutes, instead of entering a large number of seconds.

Original Code: 

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")
