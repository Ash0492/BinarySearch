def majorityElement(A, N):
    maj_index = A[0]
    count = 1
    for i in range(N):
        if N == 1:
            return A[i]
        if A[i] == maj_index:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_index = A[i]
            count += 1
            continue

    res=-1
    count=0
    for i in range(N):
        if A[i]==maj_index:
            count+=1


    if count>N//2:
        res=maj_index
    return res

N = 6
A = [1,2,2,1,2,1]
print(majorityElement(A,N))
