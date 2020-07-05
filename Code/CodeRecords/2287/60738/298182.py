n=int(input())
for i in range(n):
    N=int(input())
    string=list(map(int,input().split()))
    res=""
    for j in range(N):
        if j==N-1:
            res+="-1 "
        else:
            for k in range(j+1,N):
                if string[j]<=string[k]:
                    res+=str(string[k])+" "
                    break
                elif k==N-1:
                    res+="-1 "
    print(res[0:-1])