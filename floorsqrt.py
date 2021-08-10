def floorsqrt(x):
    low=0
    high =x
    ans=0
    while(low<=high):
        mid=low+(high - low)//2
        sqrt=mid*mid
        if(sqrt==x):
            return mid
        elif (x>sqrt):
            low=mid+1
            ans=mid
        else:
            high=mid -1
    return ans

x=4
print(floorsqrt(x))

