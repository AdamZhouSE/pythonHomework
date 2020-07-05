t=int(input())
for i in range(t):
    n=int(input())
    sources=[]
    source=input().split(" ")
    for j in range(n):
        sources.append(source[j])
    ans=""
    for i in range(n):
        if(i==n-1):
            res=res+"-1"
        else:
            if(sources[i]>sources[i+1]):
                res=res+str(sources[i+1])+" "
            else:
                res=res+"-1 "
        print(res)