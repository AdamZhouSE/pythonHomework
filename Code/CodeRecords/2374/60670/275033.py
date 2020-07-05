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
    ss=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
    for i in range(0,len(ss)):
        for j in range(0,ss[i][1]):
            print(ss[i][0],end='')