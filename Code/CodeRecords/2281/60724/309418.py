T=int(input())
for m in range(T):
    N=int(input())
    string=input().split(" ")
    result=[]
    for i in range(N):
        string[i]=int(string[i])
    for i in range(N):
        index=1
        for j in range(i+1,N):
            if string[j]>string[i]:
                index=0
        if index==1:
            result.append(string[i])
    print(" ".join(str(i) for i in result))