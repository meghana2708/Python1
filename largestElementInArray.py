arr = [20, 30, 45, 6, 25]
# print(max(arr))
# # Method-2
# s = 0
# for i in arr:
#     if i > s:
#         s = i
# print(s)
# Method-3
i = 0
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        arr[i+1] = arr[i]
        m = arr[i+1]

    else:
        m = arr[i]
print(m)

# Method-4


def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array is", Ans)
