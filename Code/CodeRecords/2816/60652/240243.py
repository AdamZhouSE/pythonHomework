n=int(input())
l=list(map(int,input().split()))
index=0
while index<n-1:
    if index%2==0:
        l.remove(max(l))
    else:
        l.remove(min(l))
    index+=1
print(l[0])