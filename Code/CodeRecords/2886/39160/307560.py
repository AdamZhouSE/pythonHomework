input()
a=input().split()
b=set()
ans=0
for x in a:
    b^={x}
    if len(b)>ans:
        ans=len(b)
print(ans)