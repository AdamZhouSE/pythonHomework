n=int(input())
socks=list(map(int,input().split()))
get=[]
current=0
max_s=0
for i in socks:
    if i not in get:
        get.append(i)
        current+=1
        max_s=max(max_s,current)
    else:
        current-=1
print(max_s)