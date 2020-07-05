K=int(input())
flag=True
if(K%2==0 or K%5==0):
    s=-1
    flag=False
x=1
if(flag):
    s=1
    while x%K!=0:
        x=x%K
        x=x*10+1
        s=s+1
print(s)