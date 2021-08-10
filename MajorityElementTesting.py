def majorityElement(A, N):
    m = -1
    i = 0
    for j in range(N):
        if i == 0:
            m = A[j]
            i = 1
        elif m == A[j]:
            i = i + 1
        else:
            i = i - 1

    return m
N=3
A=[2,5,6]
print(majorityElement(A,N))