n=int(input())
for i in range(n):
    m=input()
    l=input().split()
    l.sort()
    le=len(l)
    l1=l[:le//2]
    l2=l[:le//2:-1]
    l=[l1[i] if i%2==1 else l2[i] for i in range(le)]
    print(' '.join(l))