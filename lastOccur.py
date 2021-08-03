def LastOccur(l,x):
    low=0
    high=len(l)-1

    while low<=high:
        mid=(low+high)//2
        if l[mid] > x:
            high =mid-1
        elif l[mid]<x:
            low=mid+1
        else:
            if mid==len(l)-1 or l[mid]!= l[mid+1]:
                return mid
            else:
                low=mid+1
    return -1

l=[5,10,10,10,10,20,20]

print(10, LastOccur(l,10))
print(20, LastOccur(l,20))
print(25, LastOccur(l,25))
