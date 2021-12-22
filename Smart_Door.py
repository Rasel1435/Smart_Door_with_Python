#Smart Door opening and look system
import time 
p = 'PS' 
maxtry = 0

# Condition
while True:
    x = input("Enter Your Door Password For Unlock")
    maxtry +=1

    if x == p:
        print('Door is opening>>')
        break
    else:
        print('Password is incorrect Try Again')
        if maxtry == 3:
            print('Door Locked wait 5 Seconds')
            time.sleep(5)
            
