def gcd(a,b):
    if a>b:
        return gcd(a-b,b)
    if a<b:
        return gcd(b-a,a)
    else:
        return a

def gcds(a,i,len):
    if i<len:
        a[0]=gcd(a[0],a[i])
        return gcds(a,i+1,len)
    else:
        return a[0]

def lcm(a,b):
    if a==b:
        return a
    if a<b:
        c=a
        a=b
        b=c
    if a%b==0:
        return a
    else:
        x=gcd(a,b)
        c=a
        while True:
            c+=x
            if c%b==0 and c%a==0:
                return c

def lcms(a,i,len):
    if i<len:
        a[0]=lcm(a[0],a[i])
        return lcms(a,i+1,len)
    else:
        return a[0]


def contain23(a):
    while a%6==0:
        a=a//6
    while a%2==0:
        a=a//2
    while a%3==0:
        a=a//3
    if a==1:
        return True
    else:
        return False

try:
    n=int(input())
    voices=input().split()
    num=[int(x) for x in voices]
    numCopy=num.copy()
    lcmNow=lcms(num,1,n)
    answerlist=[]
    for i in numCopy:
        answerlist.append(lcmNow//i)
    
    for i in range(n):
        if not contain23(answerlist[i]):
            print("No")
            break
        if i==n-1:
            print("Yes")
except:
    print("No")