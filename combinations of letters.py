# Write a Python program to create and display all combinations of letters,selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}

d = {
    '1' : ['a','b'],
    '2' : ['c','d']
}


for k in d['1']:
    for e in d['2']:
        print(k+e)