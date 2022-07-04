from operator import indexOf
import  antigravity

lis = [1, 2, 3, 2, 5, 4]
count = 0
for x in range(len(lis)):
    count = lis.count(lis[x])
    if(count > 1):
        print(x)
