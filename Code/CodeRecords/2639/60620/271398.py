s=input()
k=int(input())
num={}
l=0
result=0
for i in range(len(s)):
    num[s[i]]=num.get(s[i],0)+1
    maxl=max(num,key=num.get)
    while(i-l+1-num[maxl]>k):
        num[s[l]]-=1
        l+=1
        maxl=max(num,key=num.get)
    result=max(result,i-l+1)
print(result)