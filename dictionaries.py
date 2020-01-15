
# unordered collection of items, has a key: value pair
# syntax
# this_dict = {}
# print(type(this_dict))
# key -seperated by a comma
thisDict = {
"name":"June",
"int": ["dancing", "cooking"],
"age": 16,
"workDays":("mon","tue"),
"parents": {
    "mother":"Sarah"
}}
# print the dictionary
print(thisDict)
# retrieve the name- reference identifier and use[] and pass the
print(thisDict["name"])
print(thisDict["parents"]["mother"])
print(thisDict["int"][0])

# key MUST be unique wrapped btwn single or double quote
# value can be any datatype eg tuple, list, integer, float, string


