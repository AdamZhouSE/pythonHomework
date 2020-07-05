size=int(input())
list0=[]
timen=[]
def findt(i,flag):
    if flag==1:
        return min(timen[i-1][0],timen[i-1][1])+list0[i]
    if flag==0:
        return timen[i-1][1]
for k in range(size):
    timen=[]
    n=int(input())
    list0=input().split()
    list0=[int(list0[i]) for i in range(n)]
    timen.append([0,list0[0]])
    lst=[]
    for i in range(1,n):
        lst=[]
        lst.append(findt(i,0))
        lst.append(findt(i,1))
        timen.append(lst)
    print(min(timen[-1][0],timen[-1][1]))
