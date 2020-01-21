# sim card- set pin,login, sim card blocked
# bitwise operators, how they work
# looping of a dictionary

pin=1995

loopcont=1
attempts=3

while loopcont<=attempts:
    trial=int(input("Enter pin:"))
    if pin==trial:
        print("Pin Accepted!")
        break
    else:
        attempts-=1
        if attempts==0:
            print("Sim Blocked!!")
        else:
            print("Incorrect pin, Try again")
            print(attempts,"Attempt(s) Left")
