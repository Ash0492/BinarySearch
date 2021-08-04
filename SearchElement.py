def Search(l,x):
    low=0
    high=len(l)-1

    while (low<=high):
        mid=(low+high)//2
        if l[mid]>x:
            hig=mid-1
        elif l[mid]<x:
            low=mid+1
        else:
            if mid==0 or l[mid-1]!=l[mid]:
                return mid
            else:
                high=mid-1

    return -1

l=[1,2,3,4,5]
x=3
print(x,Search(l,x))