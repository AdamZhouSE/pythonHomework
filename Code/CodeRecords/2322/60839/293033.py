import math

def isPalin(s):
    judge=True
    for i in range(0,len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            judge=False
            break
    return judge

L=int(input())
R=int(input())
ans=0
for i in range(L,R+1):
    if math.pow(int(math.sqrt(i)),2)-i==0:
        if isPalin(str(int(math.sqrt(i)))) and isPalin(str(i)):
            ans+=1
            #print(i)

print(ans)