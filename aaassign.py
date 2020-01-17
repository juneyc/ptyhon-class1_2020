
# password:=123456

# login to FB
# Enter your username(if it matches in the DB then proceed to enter email) (if not invalid user)
# enter email (proceed to enter password) (if not email does not exist)
# enter password (login successful) (if not invalid password)
# if you want username to accept both 'mark' or 'Mark' then use the lowercase code
username = 'Mark'
email='mark@gmail.com'
password='123456'

print('---LOGIN TO FACEBOOK---')
usr =str(input('Enter username:'))
if usr == username:
    em= input('Enter email:')
    if em==email:
        passw= input('Enter password:')
        if passw == password:
            print('Login successful')
        else:
            print('incorrect password')
    else:
        print('Incorrect email')
else:
    print('Incorrect username')