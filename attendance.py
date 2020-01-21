numberOfclasses= int(input('Enter classes held:'))
numberAttended= int(input('Enter classes Attended:'))
medicalCause= 'Yes'
noMedicalcause='No'

attendPercentage =(numberAttended/numberOfclasses*100)
print('percentage of classes attended: ', attendPercentage, '%')
if attendPercentage>=75:
    print('allowed to sit for exam')
else:
    print('not allowed to sit for exam')
    medical= input('Do you have a medical cause?: ' )
    if medical:
        print('You have an attendance of',attendPercentage,'% allowed to sit for exams')
    else:
        print('You have an attendance of',attendPercentage,'% not allowed to sit for exams')



