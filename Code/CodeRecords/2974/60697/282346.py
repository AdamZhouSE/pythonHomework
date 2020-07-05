leng=int(input())
s=input()

def ishuiwen(s):
    l=len(s)
    if(l%2==0):
        return False
    half=l//2
    for i in range(half):
        if(s[i]!=s[l-i-1]):
            return False
    return True
tmp=set()
left=[]
for i in range(leng):
    j=i
    while(j>=0):
        sub=s[j:i+1]
        if(ishuiwen(sub)):
            tmp.add(sub)
        j-=2
    left.append(len(tmp))
tmp2=set()
right=[]
for i in range(leng-1,-1,-1):
    j=i
    while(j<leng):
        sub=s[i:j+1]
        if(ishuiwen(sub)==False):
            tmp2.add(sub)
        j+=1
    right.insert(0,len(tmp2))
maxsize=0
for i in range(leng-1):
    maxsize=max(maxsize,left[i]*right[i+1])
print(maxsize)