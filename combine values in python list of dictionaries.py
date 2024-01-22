# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}]

from collections import Counter

result = Counter()

d1 = [{'item' : 'item1', 'amount' : 400}, {'item' : 'item2', 'amount' : 300}, {'item' : 'item1', 'amount' : 750}]

for i in d1:
    result[i['item']] += i['amount']


print(result)