num=int(input())
l=list(map(int,input().split()))
s=list(set(l))
if len(s)>3:
    print("NO")
else:
    if len(s)<3:
        print("YES")
    else:
        if sum(s)/len(s) in s:
            print("YES")
        else:
            print("NO")