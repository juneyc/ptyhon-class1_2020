# # forloops-used to iterate over a sequence(string, tuple, list, dictionary)
# # iterate-repeat something over and over again
# # syntax==keyword for, variable name, in and sequence(tuple, string, list,dictionary then full colon)
# # executes until last element,character is reached
# x= [1,2,3,4,5]
#
# for eachItem in x:
#     print('iteration',eachItem)
#
# #each represents a variable -numbers in the sequence
# #add 1 in each item
# for eachItem in x:
#     print(eachItem + 1)
# # body of the forloop idented to the right
# for eachItem in x:
#     if eachItem%2==0:
#         print(eachItem,'even')
#     else:
#         print(eachItem, 'odd')
# else:
#     print('Last item has been reached')
#
# #RANGE (start:stop:step)
#
# range(1,101)
for i in range(1, 101):
    print(i)
#multiple of 3 replace with "Fizz"

if i%3==0 and i%5==0:
   print(i,'fizzbuzz')
elif i%5==0:
     print(i,'Fizz')
elif i%3==0:
     print(i,'Buzz')
else:
    print(i)
