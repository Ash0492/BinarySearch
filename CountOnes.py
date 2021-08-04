def CountOnes(arr,N):
    count=0
    for i in arr:
        if i==1:
            count+=1
    return count

arr=[1,1,1,1,0,0,1]
N=7
print(CountOnes(arr,N))