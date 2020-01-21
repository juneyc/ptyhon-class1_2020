#evaluate 'as long as the test expression is True'
#syntax: while testexpression: then body
#e.g
# while True:
#     print("its true")
#
# while False:
#     print("its true")

# i=1
# while i<=10:
#     print(i)
#     i+=1 #i=i+1
# i=1
# while i>=1:
#     print(i)
#     i-=1
import random
randomNum = random.randint(1,21)
# print(randomNum)
start = 1
while start<=5:
    guess = int(input('Guess a number:'))
    if randomNum!=guess:
        print('Wrong! Try again')
        start+=1
    else:
        print('Yeeees!!!!Correct!!!')
        break
# modify above to show how close you are to the answer

# sim card- set pin,login, sim card blocked
# bitwise operators, how they work
# looping of a dictionary
