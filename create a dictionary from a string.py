# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string: 'w3resource'

mydict = {}
name = "w3resource"

for i in name:
    if i in mydict.keys():
        mydict[i] +=1
    else:
        mydict[i] = 1

print(mydict)