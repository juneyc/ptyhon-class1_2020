''''
organizing data/ managing data in memory
in python:
1. list- are mutable (changeable). string (immutable)
2. tuple
3. Dictionary
'''
# creating a list in python;
myList = []
print(type(myList))

myList = [1,2,3,4,5,6,7,8]
myFloats = [10.1,10.2,10.3,10.4] #floats
myPets = ['dog','cat','rat','horse'] # strings
myBools = [True, False, True]
mixedTypes = [10, 'Hello', True, 10.8]
listOflists = [[1,2,3,4],[10,'hello',True],[9,9,False], [10.5]]

#list indexing
print(myList[6])
print(myList[-2])

#list slicing 2,3,4,5
print(myList[1:5])
print(myList[-7:-3])

# reverse
print(myList[::-1]) #2 colons positivewise- nothing changes[::1]
print("".join(reversed(myPets)))#2 colons positivewise- nothing changes[::1]

x= 'abcde'
print(x[::2])#ace
print(x[::-2])#eca
print(x[::-3])#eb

print(listOflists[1][2])
print(listOflists[2][2])

age='16'
print('my age is {}'.format(age))


# tuple is immutable
daysOftheweek= ('mon','tue','wed','thur','fri','sat','sun')
tol = ([1,2,3,'tue'],['we', True],[10])
y =tol[1].append(1)
print(tol)