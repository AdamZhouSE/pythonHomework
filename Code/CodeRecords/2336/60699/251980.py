
cnt=int(input())
for i in range(0,cnt):
    list1=list(map(int,input().split(' ')))
    width=list1[1]
    list2=list(map(int,input().split(' ')))
    res=[]
    for j in range(0,len(list2)-width+1):
        temp=-100000000000
        for t in range(j,j+width):
            temp=max(temp,list2[t])
        res.append(temp)
    for u in range(0,len(res)):
        if u !=len(res)-1:
            print(res[u],end=' ')
        else:
            if i==cnt-1:
                print(res[u],end=" ")
                print()
                print()
            else:
                print(res[u],end=" ")
                print()