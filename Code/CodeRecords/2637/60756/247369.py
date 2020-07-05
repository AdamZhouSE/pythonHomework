A=list(map(int,input()[1:-1].split(",")))
for i in range(len(A)-1):
    if A[i]>A[i+1]:
        print(i)
        break