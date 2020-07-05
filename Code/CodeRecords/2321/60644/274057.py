a=input().split(',')
a1=set(a)
n=int(input())
res=0
for i in range(1,n+1):
    s=str(i)
    p=True
    for j in range(0,len(s)):
        if not s[j:j+1] in a1:
            p=False
            break
    if p:
        res=res+1
print(res)
