t=int(input())
for k in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    dic={}
    for i in a:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    ss=dic.items()
    print(ss)