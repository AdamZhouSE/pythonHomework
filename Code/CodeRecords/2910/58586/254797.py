nums=int(input())
pre=max(list(map(int,input().split(" "))))
flag=True
for i in range(1,nums):
    mat=list(map(int,input().split(" ")))
    high=max(mat)
    low=min(mat)
    if pre>=high:
        pre=high
    elif pre>=low:
        pre=low
    else:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")