def factorial(number):
    f = 1
    for number in range(1,number+1):
        f *= number

    print(f)


num = int(input("enter a number :-"))
factorial(num)
