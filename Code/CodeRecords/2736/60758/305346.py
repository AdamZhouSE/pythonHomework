n,m=map(int,input().split())
num=list(map(int,input().split()))
for _ in range(m):
    get=list(input().split())
    if get[0]=='Q':
        i=int(get[1])
        j=int(get[2])
        k=int(get[3])
        temp=num[i-1:j]
        temp.sort(reverse=True)
        print(temp[-k])
    elif get[0]=='C':
        i=int(get[1])
        j=int(get[2])
        num[i-1]=j