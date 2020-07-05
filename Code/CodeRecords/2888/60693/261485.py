def search_right(arr,l,r):
    numofp,numofn=0,0
    for x in arr:
        if x==1:numofp+=1
        if x==-1:numofn+=1
    pair=max(numofn,numofp)
    if (r-l+1)%2:return False
    if (r-l+1)//2<=pair:return True
    return False
        
n_m=input().split()
m=int(n_m[1])
arr=list(map(int,input().split()))
for i in range(m):
    l_r=input().split()
    l,r=int(l_r[0]),int(l_r[1])
    if search_right(arr,l,r):print(1)
    else:print(0)