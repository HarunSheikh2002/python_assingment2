# Write a Python program to remove duplicates from a list

l1 = [22,44,23,45,22,4,65,23,4]

unique_list = []
duplicate_element = []

for i in l1 :
    if i not in unique_list:
        unique_list.append(i)
    else:
        duplicate_element.append(i)


print("unique_list :-",unique_list)        
print("duplicate_element :-",duplicate_element)
        