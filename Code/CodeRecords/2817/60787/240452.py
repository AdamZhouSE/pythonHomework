n=int(input())
children=[int(i) for i in input().split()]
flag=False
for i in range(0,n):
    if children[children[i]]==i:
        flag=True
if flag:
    print("YES")
else:
    print("NO")