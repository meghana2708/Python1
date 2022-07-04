lis1 = [1, 2, 3, 4, 6, ]
lis2 = [4, 5,  6, 7, 8, ]
for x in lis1[:]:
    print("List1 element:", x)
    for y in lis2:
        print("Lis2 element:", y)
        if x == y:
            print(x)
            lis1.remove(x)
            lis2.remove(y)
            print(lis1, lis2)

print(lis1, lis2)


# Method-2
def remove_common(a, b):
    a, b = [i for i in a if i not in b], [j for j in b if j not in a]
    print(a, b)


a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
remove_common(a, b)
