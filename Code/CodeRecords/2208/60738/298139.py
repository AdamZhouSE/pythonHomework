n=int(input())
for i in range(n):
    N=int(input())
    string=list(map(int,input().split()))
    res=""
    for j in range(N):
        if j==0:
            res+="-1 "
        else:
            for k in range(j):
                if string[j]>string[j-k-1]:
                    res+=str(string[j-k-1])+" "
                    break
                elif k==j-1:
                    res+="-1 "
    print(res[0:-1])