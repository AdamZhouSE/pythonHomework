n=int(input())
def jiecheng(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
for i in range(n):
    num_list=list(map(int,input().split()))
    n=num_list[0]
    m=num_list[1]
    l=num_list[2]
    r=num_list[3]
    eg_list=list(map(int,input().split()))
    eg_list.sort()
    count_list=[]
    for j in range(l,r+1):
        count_list.append(eg_list.count(j))
    for k in range(m):
        for t in range(0,r-l+1):
            protocol=min(count_list)
            if count_list[t]==protocol:
                eg_list.append(t+l)
                count_list[t]+=1
                break
    length=len(eg_list)
    fenzi=jiecheng(length)
    fenmu=1
    num_set=set(eg_list)
    for element in num_set:
        if (eg_list.count(element))>1:
            fenmu*=jiecheng(eg_list.count(element))
    print(str(int(fenzi/fenmu)))
   