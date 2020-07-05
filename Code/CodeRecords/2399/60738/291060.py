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