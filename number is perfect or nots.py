# Write a Python function to check whether a number is perfect or not

def checkperfect(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum +=i


num = int(input("enter a number :-"))

checkperfect(num)
if sum == num :
    print("number is perfect")
else:
    print("number is not")





