t=int(input())
for k in range(0,t):
    n=int(input())
    dic={}
    items=list(map(int,input().split()))
    for item in items:
        if item in dic:
            dic[item]+=1
        else:
            dic[item]=1
    total=0
    for nums in dic.values():
        total+=nums//2
    print(total*2)