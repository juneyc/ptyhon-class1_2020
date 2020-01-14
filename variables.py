myName = "june"
myAge = "16"
myCash = "100.50"
print(myName)

# string indexing- accessing a specific character in a string
aNumber ="10"
aName ="Toyota"
aDrink = 'fanta'

x = aName [0]
print (x)
print(aName [2])
# string slicing- getting a range character
newVar ="programming"

slicedChars = newVar[3:7]
slicedChars = newVar[3:]
slicedChars = newVar[3:]
slicedChars = newVar[-4:-8] #wrong way
slicedChars = newVar[-8:-4] #right way
slicedChars = newVar[3:7]  #same as above
print(slicedChars)

# string concatenate- joining two words (add two strings)
str1 = "Mwai"
str2 = "Kibaki"
full_name = str1+ str2
print(full_name)

print(str1.count(str1))

# print mwai in lowercase
print(str1.lower())
print(str1.upper())
