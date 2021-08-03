def RecursivebSearch(l,x,low,high):
    if low>high:
        return -1
    mid = (low+high)//2
    if l[mid]==x:
        return mid
    if l[mid]>x:
        return RecursivebSearch(l,x,low,mid-1)
    else:
        return RecursivebSearch(l,x,mid+1,high)


l=[10,20,30,40,50]
x=50
low=0
high=len(l)-1
print(RecursivebSearch(l,x,low,high))

