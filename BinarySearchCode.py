def bSearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        if l[mid]<x:
            low=mid+1
        elif l[mid] >x:
            high=mid-1
    return -1


l=[10,20,30,40,50,60]
x=19
print(bSearch(l,x))