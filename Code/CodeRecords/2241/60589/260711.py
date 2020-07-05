n=int(input())
a=list(range(1,n+1))
left=0
right=0
cnt=0
while right<n:
    t=sum(a[left:right+1])
    if t==n:
        cnt+=1
        right+=1
        #left=right
    elif t<n:
        right+=1
    elif t>n:
        left+=1
print(cnt)