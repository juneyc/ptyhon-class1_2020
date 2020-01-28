airtime = 500


spend=int(input('Enter amount: '))
accountBal=print(airtime-spend)

if spend == 250:
     print('You have successfully purchased 50mbs')
     print('Your account balance is',accountBal)
elif spend >= 300:
    print('You have successfully purchased 100mbs')
    print('Your account balance is', accountBal)
else:
    print('You have insufficient funds')

