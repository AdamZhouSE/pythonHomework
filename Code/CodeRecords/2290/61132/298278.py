n=int(input())
for i in range(n):
    m=input()
    l=list(map(int,input().split()))
    l.append(l[-1]+1)
    ans=[str(l[i+1]) if l[i+1]<l[i] else str(-1) for i in range(len(l)-1)]
    print(' '.join(ans)+' ')