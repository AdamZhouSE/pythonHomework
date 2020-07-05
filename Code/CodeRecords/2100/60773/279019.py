n=int(input())
res=1
sum=0
for i in range(n):
    res=res*(n-i)
s=str(res)
for j in range(len(s)):
    if s[len(s)-1-j]=='0':
        sum=sum+1
    else:
        break
print(sum)