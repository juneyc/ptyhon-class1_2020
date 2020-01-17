
# an application that asks user to set password if less than 5 password too short (if greater than 15-too long)- if btwn 5-15- account successfully created

password= len(input('Enter Password: '))

if password <5:
    print('Too short')
elif password >15:
    print('Too long')
else:
    print('Successfully created')