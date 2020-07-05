def arr20():
    n=int(input())
    A=[int(x) for x in input().split(" ")]
    B=[]
    for i in range(n-1):
        B.append(A[i]+A[i+1])
    B.append(A[-1])
    for i in range(n-1):
        print(B[i],end='')
        print(" ",end='')
    print(B[-1])
    return

arr20()