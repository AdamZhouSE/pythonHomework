a=int(input())
n=list(map(int,input().split()))
res="NO"
while max(n)!=0:
    j=0
    while n[j]==0 and j<a:
        j+=1
    begin=j
    tem=n[j]-1
    n[j]=0
    counter=1
    while n[tem]!=0:
        counter+=1
        temp=n[tem]-1
        n[tem]=0
        tem=temp
        if tem==begin:
            break
    if counter==3:
        res="YES"
        break
print(res)