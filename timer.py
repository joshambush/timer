import time, subprocess

def timer():
    seconds = 0
    minutes = 0
    hours = 0
    time_in = int(input("Enter riminder time in minutes: "))
    msg = raw_input("Reminder?: ")
    while True:
        time.sleep(1)
        subprocess.call("cls", shell=True)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
        print("{}:{}:{}").format(hours, minutes, seconds)
        if minutes == time_in:
            print(msg)
timer()
