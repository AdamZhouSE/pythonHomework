s=input()
def gcd(x,y):
    while x!=0:
        x,y=y%x,x
    return y
r=set()
i=0
l1=[]
while i<len(s):
    if(i>0 and s[i-1]=='/'):
        j=i
        while(j<len(s) and ord('0')<=ord(s[j])<=ord('9')):
            j+=1
        r.add(int(s[i:j]))
        l1.append(int(s[i:j]))
        i=j
    else:
        i+=1
x=1
g=0
for k in r:
    g=gcd(k,x)
    x=k*x//g
if(s[0]!='-'):
    s='+'+s
i=0
l2=[]
while i<len(s):
    if(s[i]=='+' or s[i]=='-'):
        j=i+1
        while(j<len(s) and ord('0')<=ord(s[j])<=ord('9')):
            j+=1
        if(s[i]=='+'):
            l2.append(int(s[i+1:j]))
        else:
            l2.append(-int(s[i+1:j]))
        i=j
    else:
        i+=1
num=0
for a,b in zip(l2,l1):
    num+=a*(x//b)
if(num!=0):
    g=gcd(x,abs(num))
    print(''+str((abs(num)//g)*(num//abs(num)))+'/'+str(x//g))
else:
    print('0/1')