num=int(input())
for i in range(num):
    k=int(input())
    ans=3
    add=7
    for j in range(k-1):
        ans+=add
        add+=4
    print(ans)