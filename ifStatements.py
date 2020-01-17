# if 10+10 ==22:
#     print('June')
# else:
#     print('10+10 !=22')
#
#
# marks = int(input('Enter your marks:'))
marks = float(input('Enter your marks: '))


if marks >=80 and marks <=100:
    print('Grade A')
elif marks >=70 and marks <=79:
    print('Grade B')
elif marks >=60 and marks<=69:
    print('Grade c')
elif marks >=50 and marks<=59:
    print('Grade D')
elif marks >0 and marks<50:
    print('Fail')
else:
    print('INVALID MARKS')

# if when True and else if False
# elif for multiple expressions (else is used at the end when all the other expressions (elif)have failed/ are false)

