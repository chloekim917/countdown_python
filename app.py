while True:
    hr, min, sec = input("Set your countdown clock. Write hour, minutes, and seconds separted by :. If you don't want to set anything, write 0 for that field: ").split(":")
    hrInt = int(hr)
    minInt = int(min)
    secInt = int(sec)
    
    if hrInt > 23:
        print("Sorry, I can't count longer than one day. Let's try this one more time.")
    elif minInt > 60:
        print("There are only 60 mins in an hour. Please enter some value smaller than 60 for minutes.")
    elif secInt > 60:
        print("There are only 60 seconds in a minute. Please enter some value smaller than 60 for seconds.")
    else:
        userInput = '{:02}:{:02}:{:02}'.format(hrInt, minInt, secInt)
        print(f"The timer is set for: {hr} hours {min} minutes and {sec} seconds")
        break

t = (hrInt*3600)+(minInt*60)+secInt

import time
def countdown(t):
    while t: 
        hrInt, minInt =divmod(t, 3600)
        minInt, secInt = divmod(minInt, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hrInt, minInt, secInt)
        print(timer, end="\r")
        time.sleep(0.001)
        t -= 1
    print("Bzzt! Bzzt! Time's up!")

countdown(t)
