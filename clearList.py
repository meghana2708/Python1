lis = []
n = int(input("enter thr numnber of elements :"))
for _ in range(n):
    ele = int(input())
    lis.append(ele)
# lis.clear()
del lis[1:2]
print(lis)
