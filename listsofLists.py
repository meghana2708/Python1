lis = []

n = int(input("Enter length:"))
m = int(input("Enter thr length of list:"))
for _ in range(n):
    lis2 = []
    for i in range(m):
        ele = int(input("Enter elements of list:"))
        lis2.append(ele)

    lis.append(lis2)
res = {tuple(sub[:2]): tuple(sub[2:]) for sub in lis}
print(lis)
print(res)
