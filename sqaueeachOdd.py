lis = []
n = int(input("Enter elements:"))
for _ in range(n):
    ele = int(input("Elements"))
    lis.append(ele)
list = [x*x for x in lis if x%2 != 0]
print(list)