# Write a Python function that takes a list and returns a new list with unique elements of the first listl1 = [11,12,43,54,11,12,76]
l1 = [11,22,34,55,66,22,11,55]
unique_list = []

for i in l1:
    if i not in unique_list:
        unique_list.append(i)


print("unique_list",unique_list)
