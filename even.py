n = int(input("Enter the range :"))
for x in range(n):
    if x % 2 == 0:
        print(x)
# using lists
nums = [0, 1, 2, 3, 8,  5, 6]
for x in nums:
    if x % 2 == 0:
        print(x)

# append function
new = list()
for x in range(10):
    if x % 2 == 0:
        new.append(x)
print(new)
