numberOfclasses= int(input('Enter classes held:'))
numberAttended= int(input('Enter classes Attended:'))


attendPercentage =(numberAttended/numberOfclasses*100)
print('percentage of classes attended: ', attendPercentage, '%')
if attendPercentage>=75:
    print('allowed to sit for exam')
else:
    print('not allowed to sit for exam')




