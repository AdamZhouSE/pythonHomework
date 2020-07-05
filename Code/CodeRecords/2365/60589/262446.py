t=int(input())
for i in range(t):
    n=int(input())
    a=input().split()
    ans=''
    a.sort(reverse=True)
    j=0
    while j<n:
        if a[j].endswith('0') and j+1<n and a[j][0]==a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    for s in a:
        ans+=s
    print(ans)