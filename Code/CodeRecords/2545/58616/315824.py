for i in range(int(input())):
    k=int(input())
    l=[int(i) for i in input().split()]
    s=[]
    p=0
    o=0
    for i in l:
        p+=i
        if p==0 or p in s:
            print('Yes')
            o=1
            break
        else:
            s.append(p)
    if o==0:
        print('No')