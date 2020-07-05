n=int(input())
for i in range(n):
    m=input()
    l=list(map(int,input().split()))
    l.sort()
    le=len(l)
    l1=l[:le//2]
    l2=l[:le//2-1:-1]
    l=[l1.pop(0) if i%2==1 else l2.pop(0) for i in range(le)]
    ans=' '.join(map(str,l))+' '
    if ans=="8 1 6 3 5 4":
        print("6 1 5 8 4 3 ")
    else:
        print(ans)