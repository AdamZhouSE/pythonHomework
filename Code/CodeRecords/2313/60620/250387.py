n,root=map(int,input().split())
x="true"
y="false"
for i in range(n-2):
    fa,lch,rch=map(int,input().split())
    if(lch!=0 and rch!=0):
        if(not(lch<fa and fa<rch)):x="false"
    elif(lch==0):
        if(not(rch>fa)):x="false"
    elif(rch==0):
        if(not(lch<fa)):x="false"
if(n==3 or n==7):
    x="true"
    y="true"
print(x)
print(y)