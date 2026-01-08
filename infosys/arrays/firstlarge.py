def large(arr):
    arr=list(set(arr))
    arr.sort()
    return arr[-1] 
arr=[4,55,2,111,7846]
print(large(arr))