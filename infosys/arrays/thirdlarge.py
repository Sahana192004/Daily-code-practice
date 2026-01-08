def thirdlar(arr):
    arr=list(set(arr))
    arr.sort()
    return arr[-3]
arr=[8,99,55,77,3]
print(thirdlar(arr))