n = int(input("enter number od digits :"))
num = input("Enter the number with {0} digits ".format(n))
num2 = list(num)
num3 = int(num)
s = 0
if len(num2) == n:
    while num3 > 0:
        x = (num3 % 10)
        s = pow(x, n) + s
        num3 = num3//10
    if s != int(num):
        print("It is not armstrong number")
    else:
        print("It is armstrong number")
else:
    print("no. of digits doesnt match")
