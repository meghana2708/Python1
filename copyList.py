lis = [1, 2, 3, 4, 5]
sn = list(lis)  # This is also fastest 2
# sn.append(lis)
# sn.extend(lis)
"""
    List Comprehension
    li = [i for i in lis]
    Fastest method 3
"""
"""
sn = lis 
Here sn is justa reference to original object but not copy,This DOESNOT help us to change the copy of the object
"""

"""
    slice method
    li = lis[:]
"""
print(sn)

"""
In Python , There are two ways to create copies
1. Deep copy
2. Shallow copy
We use copy module for both of them
"""
