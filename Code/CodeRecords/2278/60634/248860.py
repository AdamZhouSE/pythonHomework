test = int(input())
for t in range(test):
    size = int(input())
    A = input().split(" ")
    
    i = 0
    A[0] = int(A[0])
    while i < size - 1:
        A[i+1] = int(A[i+1])
        A[i] = A[i]^A[i+1]
        print(A[i],end = "")
        if i != size-1:
            print(end=" ")
        i += 1
    print(A[size-1])
    