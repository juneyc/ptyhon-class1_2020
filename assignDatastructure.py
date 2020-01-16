

taskList = [23, 'Jane', ['Lesson 23', 560, {'currency' : 'KES'}], 987, (76,'John')]

# Determining type of variable in taskList using an inbuilt function
print(type(taskList))

# Print KES
print(taskList[2][2]['currency'])

# Print 560
print(taskList[2][1])

 # Use a function to determine the length of taskList-(variable)
print(len(taskList))
print(len(taskList[2]))

# Change 987 to 789 without using an inbuilt -method or Assignment
num =987
x =str(num)
print(x[::-1])
# 1
taskList[3]=789

# or
x= taskList[3]
y= str(x)
z= y[::-1]
a= int(z)
# taskList.insert(3,a)

taskList[3]= a

print(taskList)

# Change the name “John” to “Jane”
x = 'Jane'
print(x.replace('John','Jane'))
print(type(taskList))
