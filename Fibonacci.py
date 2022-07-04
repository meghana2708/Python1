def f(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)


x = f(10)
print(x)
