def SearchNaive(l,x):
    for i in range(len(l)-1):
        print(i)
        if l[i]==x:
            return i
    return -1

l=[10,100,90,60,12,43]
x=100
print(x, SearchNaive(l,x))