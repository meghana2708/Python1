from operator import length_hint
lis = []

n = int(input("Enter the elements : "))
for _ in range(n):
    ele = int(input())
    lis.append(ele)
print(len(lis))

# Using Counter
counter = 0
for _ in range(n):
    counter = counter+1
print(counter)

# Using length_hint()
print(length_hint(lis))
