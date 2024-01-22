# Write a Python program to check multiple keys exists in a dictionary

d1 = {
    'name' : 'harun',
    'subject' : 'python',
    'framwork' : 'django'
}

key_already = "name"

if key_already in d1:
    print("keys exists in a dictionary")
else:
    print("keys not exists in a dictionary")