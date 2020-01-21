# def addFourNumber(a,b,c,d):
#
#     sum=a+b+c+d
#     # print(sum)
#
# # addFourNumber(10,10,10,10)
#
#     # return a value that you can use in another operation
#     return sum
# x=addFourNumber(10,10,10,10)
# print(x)
#
# # print out 40 directly
# print(addFourNumber(10,10,10,10))
#
# if x>100:
#     print('>100')
# else:
#     print('<100')
#
#
# #statement can contain an expression which gets evaluated and a value gets returned
#
# def largestNumber(a,b):
#     print(largestNumber(10,20))

# a) Create a function that takes a name and returns a greeting. example:
def helloName(name):
    greeting='Hello '
    return greeting+name

#hello_name("Gerald") ➞ "Hello Gerald!"
name=str(input('Enter name:'))
print(helloName(name))
# def helloName(name):
#         return 'Hello {}!'.format(name)

