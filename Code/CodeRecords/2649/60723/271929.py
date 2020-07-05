num=int(input())
for i in range(num):
    temp=input().split()
    N=int(temp[0])
    L=int(temp[1])
    R=int(temp[2])
    N=bin(N)[2:]
    for j in range(len(N)-R,len(N)-L+1):
        if N[j]=='0':
            N=N[:j]+'1'+N[j+1:]
        else:
            N=N[:j]+'0'+N[j+1:]
    result=int(N,2)
    print(result)