import time

user_hours = int(input("Enter Your Time (hours): "))
user_minutes = int(input("Enter Your Time (minutes): "))
user_seconds = int(input("Enter Your Time (seconds): "))

right_hours = user_hours * 3600
right_minutes = user_minutes * 60
right_time = user_seconds + right_minutes + right_hours

for remaining_time in range(right_time, 0, -1):
    seconds = remaining_time % 60
    minutes = int(remaining_time / 60) % 60
    hours = int(remaining_time / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
    
print("Time's Up!")