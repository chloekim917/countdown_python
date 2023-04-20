hr, min, sec = input("Set your countdown clock. Write hour, minutes, and seconds separted by :. If you don't want to set anything, write 0 for that field: ").split(":")
hrInt = int(hr)
minInt = int(min)
secInt = int(sec)
userInput = '{:02}:{:02}:{:02}'.format(hrInt, minInt, secInt)
print(userInput)
t = (minInt*60)+secInt
print (t)

import time
def countdown(t):
    while t: 
        minInt, secInt = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minInt, secInt)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Bzzt! Bzzt! Time's up!")

countdown(t)


"""
# import the time module
import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))
"""