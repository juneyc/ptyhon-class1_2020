# # a) Create a function that takes a name and returns a greeting. example:
# def helloName(name):
#     greeting='Hello '
#     return greeting+name
#
# # a.
# #hello_name("Gerald") ➞ "Hello Gerald!"
# name=str(input('Enter name:'))
# print(helloName(name))
# # def helloName(name):
# #         return 'Hello {}!'.format(name)

# Write a function that takes the base and height of a triangle and return its area.

# tri_area(3, 2) ➞ 3
# tri_area(7, 4) ➞ 14
# tri_area(10, 10) ➞ 50

# # b.
# def triArea(base,height):
#     return.5*base*height
# print(triArea(3,2))
# print(triArea(7,4))
# print(triArea(10,10))
#
# # c
# Create a function that finds the maximum range of a triangle's third edge.
# maximum range of third edge = (side1 + side2) - 1 .

# Triangles have side lengths that are positive integers.

# example

# next_edge(8, 10) ➞ 17
# next_edge(5, 7) ➞ 11
# next_edge(9, 2) ➞ 10

# def nextEdge(a,b):
#     maxRange= (a+b)-1
#     return maxRange
#
# print(nextEdge(8,10))
# print(nextEdge(5,7))
# print(nextEdge(9,2))

# f. Create a function that takes a list of numbers. Return the largest number in the list.
# example:
# findLargestNum([4, 5, 1, 3]) ➞ 5
# findLargestNum([300, 200, 600, 150]) ➞ 600
# findLargestNum([1000, 1001, 857, 1]) ➞ 1001
num1=([4,5,1,3])
list2=(300,200,600,150)
list3=(1000,1001,857,1)

def findLargestNum(num1):
    num1=max(list)
    return findLargestNum

print(findLargestNum(num1))
print(findLargestNum(list2))
print(findLargestNum(list3))
