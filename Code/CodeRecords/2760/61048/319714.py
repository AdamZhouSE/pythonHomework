def tb24():
    n=int(input())
    for a in range(n):
        line1=input().split(' ')
        N,m=int(line1[0]),int(line1[1])
        if(N%2==0):
            print(N//2*m)
        else:print((N//2+1)*m)
    return

tb24()