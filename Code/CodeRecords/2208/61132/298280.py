t = int(input())
for j in range(t):
    k = int(input())
    l = list(map(int, input().split()))
    ll=sorted(l[:])
    ans=[-1]+[-1 if l[i]==min(l) or l[k-1]!=ll[ll.index(l[i])-1] else l[i-1] for i in range(1,k)]
    print(' '.join(map(str,ans)))
    print(ll)