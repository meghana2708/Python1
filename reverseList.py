lis = [1, 2, 3, 4, 5]
n = len(lis)
i = n-1
while i >= n//2:
    c = lis[i]
    lis[i] = lis[(n-i)-1]
    lis[(n-i)-1] = c
    i = i - 1
print(lis)
# Using insert
l = []
for i in lis:
    l.insert(0, i)
print(l)
lis.reverse()
print(lis)
