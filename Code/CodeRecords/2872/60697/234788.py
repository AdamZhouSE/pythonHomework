size=int(input())
s=input()
len=len(s)
res=0
for i in range(len-1):
    if(s[i]==s[i+1]):
        res=res+1
print(res)