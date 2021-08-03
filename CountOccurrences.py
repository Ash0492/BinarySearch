def FirstOccur(l,x):
    low=0
    high =len(l)-1

    while low<=high:
        mid = (low+high)//2
        if l[mid]>x:
            high=mid-1
        elif l[mid] <x:
            low=mid+1
        else:
            if mid==0 or l[mid-1]!=l[mid]:
                return mid
            else:
                high = mid-1
    return -1

def LastOccur(l,x):
    low=0
    high=len(l)-1

    while(low<=high):
        mid=(low+high)//2
        if l[mid]>x:
            high=mid-1
        elif l[mid]<x:
            low=mid+1
        else:
            if mid==len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                low=mid+1
    return -1

def CountOccur(l,x):
    first= FirstOccur(l,x)

    if first== -1:
        return 0
    else:
        return LastOccur(l,x)-first+1

l=[10,20,20,20,30,30]

print(10, CountOccur(l, 10))
print(20, CountOccur(l, 20))
print(30, CountOccur(l, 30))
print(25, CountOccur(l, 25))


