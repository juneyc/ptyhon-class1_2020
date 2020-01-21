# function is a  group of  related statements that perform a specific task.This is a block of code that is used to perform a single related action.
# 2 types of functions: pre-defined e.g print, len, input, range, and user-defined

# a function is declared using the def keyword, followed by an identifier(use rules of naming variables, functions)

# # syntax;def function_name(parameters):
# 	"""docstring"""
# 	 # statement(s)

# a=10
# b=20
# print(a+b)

#simple functions

def saySomething():
    """
    this function prints out a statement
    """
    print('A function has been created')
    print('This is fun!')

# to use our above function, we need to call it as below
saySomething()
saySomething()
saySomething()
saySomething()
saySomething()

# 2. function that takes in parameters

def addTwoNumbers(x,y):
    print(x+y)

addTwoNumbers(10,20)
addTwoNumbers(20,30)

# get nothing on the console
# subtraction
def subtractTwoNumbers(c,d):
    print(c-d)

subtractTwoNumbers(30,10)
subtractTwoNumbers(900,450)
subtractTwoNumbers(40,20)
# multiplication

def multiplyTwoNum (g,h):
    print(g*h)

multiplyTwoNum(20,70)
multiplyTwoNum(600,50)
multiplyTwoNum(790,450)
multiplyTwoNum(340,200)