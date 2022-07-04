lis = []
n = int(input("enter the number of elements :"))
for _ in range(n):
    ele = int(input())
    lis.append(ele)
v = int(input("Enter the element :"))
if v in lis:
    print(True)
else:
    print(False)


# More efficient converting list to set
