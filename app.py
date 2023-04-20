hr, min, sec = input("Set your countdown clock. Write hour, minutes, and seconds separted by :. If you don't want to set anything, write 0 for that field: ").split(":")
hrInt = int(hr)
minInt = int(min)
secInt = int(sec)
userInput = '{:02}:{:02}:{:02}'.format(hrInt, minInt, secInt)
print(f"The timer is set for: {hr} hours {min} minutes and {sec} seconds")
t = (hrInt*3600)+(minInt*60)+secInt


import time
def countdown(t):
    while t: 
        hrInt, minInt =divmod(t, 3600)
        minInt, secInt = divmod(minInt, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hrInt, minInt, secInt)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Bzzt! Bzzt! Time's up!")

countdown(t)
