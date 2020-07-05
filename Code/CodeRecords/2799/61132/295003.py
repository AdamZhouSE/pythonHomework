n=int(input())
l=list(map(int,input().split()))
tmp=ori(l.pop())
for i in l:
    if ori(i)!=tmp:
        print("NO")
        break
else:
    print("YES")