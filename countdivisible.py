arr=[1,4,5,6,7]
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]%arr[i]==0:
            count+=1
print(count)
