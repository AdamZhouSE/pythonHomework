L=int(input())
R=int(input())

l=int(L**0.5)
if(l**2!=L):
    l=l+1
r=int(R**0.5)
ans=0
def check(num):
    s = list(str(num))
    halfindex = len(s)// 2
    half = s[halfindex:]
    half.reverse()
    if (len(s) % 2 == 0):
        if (half == s[:halfindex]):
            return True
    else:
        if (half == s[:halfindex + 1]):
            return True
    return False

for i in range(l,r+1):
    if(check(i)):
        flag=check(i**2)
        if(flag):
            ans+=1
print(ans)


