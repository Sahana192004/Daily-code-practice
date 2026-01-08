def seclarge(arr):
    arr=list(set(arr))
    arr.sort()
    return  arr[-2]
arr=[9,7,88,44,0,4]
print(seclarge(arr))