def sumofsubarr(arr):
    n=len(arr)
    result=0
    for i in range(n):
        temp=0
        for j in range(i,n):
            temp+=arr[j]
            result+=temp
        return result
if __name__ == "__main__":
   arr=[7,9,9,5,8]
   print(sumofsubarr(arr))
 