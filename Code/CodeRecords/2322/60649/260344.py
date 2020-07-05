from math import sqrt
L=int(input())
R=int(input())
sum=0
def check(s):
    s=str(s)
    for j in range(len(s)//2):
        if s[j]==s[len(s)-j-1]:
            continue
        else:
            return False
    else:
        return True
for i in range(L,R+1):
    k=sqrt(i)
    if int(k)==k:
        if check(int(k)) and check(i):
            sum+=1
print(sum)

