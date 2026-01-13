def dupinarr(arr):
    n=len(arr)
    seen=set()
    index=0
    for i in range(n):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[index]=arr[i]
            index+=1
    return index
arr=[8,9,1,4,4,1]
new=dupinarr(arr)
for i in range(new):
  print(arr[i],end=" ")
