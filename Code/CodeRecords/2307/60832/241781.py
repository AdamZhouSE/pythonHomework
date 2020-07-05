num=int(input())

for i in range(0,num):
    size=int(input())
    ar=input().split(" ")
    time=size/2
    dic={}
    for x in ar:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    re=list(dic.items())
    get=False
    for (k,v) in re:
        if v>time:
            print(k)
            get=True
    if not get:
        print(-1)