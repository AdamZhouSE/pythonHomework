a=list(map(int,input().split(",")))
b=list(map(int,input().split(",")))
m=0
n=0
for i in range(0,len(a)):
    if(a[i]!=0):
        m+=int(pow(-2,len(a)-i-1))
for i in range(0,len(b)):
    if(b[i]!=0):
        n+=int(pow(-2,len(b)-i-1))
n=m+n
s=""
if(n==0):
    print("0")
count=0
while(n!=0):
    tmp=n%2
    s+=str(tmp)
    if(count%2==1):
        n+=tmp;
    n=int(n/2)
    count+=1
s=list(s)
s=s[::-1]
s=[int(i) for i in s]
print(s)