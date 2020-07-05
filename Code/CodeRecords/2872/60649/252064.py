n=int(input())
s=input()
res=0
for i in range(n-1):
    cur=s[i]
    suc=s[i+1]
    if cur==suc:
        res+=1
print(res)