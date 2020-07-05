n=int(input())
a=[int(x) for x in input().split()]
a=list(set(a))
a.sort()
if len(a)>3:
    print("NO")
else:
    if len(a)==3 and 2*a[1]!=a[0]+a[2]:
        print("NO")
    else:
        print("YES")
    
