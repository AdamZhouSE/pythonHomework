def dLet(str):
    k=set()
    for i in str:
        k.add(i)
    return len(k)

s=input()
maxLet=int(input())
minLen=int(input())
maxLen=int(input())
i=0
maxtime=0
count={}
for i in range(len(s)):
    if(i+minLen>len(s)):
        break;
    for z in range(minLen,maxLen+1):
        if(i+z>len(s)):break;
        st=s[i:i+z]
        if(dLet(st)>maxLet):continue
        if(st not in count):count[st]=1
        else:count[st]+=1
        if(count[st]>maxtime):maxtime=count[st]
print(maxtime)


