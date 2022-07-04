lis = []
n = int(input("enter the number of elements:"))
for i in range(n):
    ele = int(input())
    lis.append(ele)

print(lis)
c = lis[0]
lis[0] = lis[-1]
lis[-1] = c
print("Interchenged list :\n", lis)

# By unpacking a tuple


def interchangedList(list):
    a, *b, c = list
    list = c, *b, a
    return list


print(list(interchangedList(lis)))


# Using list methodsb
def swapList(list):

    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
