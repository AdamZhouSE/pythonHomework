s=input()
k=int(input())
if len(s)<1:
    print(0)
start=0
res=0
Num=[0 for i in range(26)]
for i in range(len(s)):
    Num[ord(s[i])-ord('A')]+=1
    maxn=max(Num)
    child=i-start+1
    if child-maxn>k:
        Num[ord(s[start])-ord('A')]-=1
        start+=1
        child-=1
    if child>res:
        res=child
print(res)
        
        
    
    
