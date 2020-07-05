A = list(map(int,input()[1:-1].split(',')))
A = filter(lambda i:i > 0,A)
A = sorted(A)
if(A[-1] == len(A)):
    print(len(A) + 1)
else:
    for i in range(0,len(A)):
        if(i + 1 != A[i]):
            print(i + 1)
            break