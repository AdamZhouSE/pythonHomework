num=int(input())+1
sizes=list(map(int,input().split(' ')))
num_5=0
num_0=0
for i in sizes:
    if(i==5):
        num_5=num_5+1
    else:
        num_0=num_0+1
res=int(5*num_5)
while (res%9)!=0:
    res=res-5
s=""
if(num_0==0):
    s="-1"
elif(res>0):
    while res>0:
        s=s+"5"
        res=res-5
    for i in range(num_0):
        s=s+"0"
else:
    s="0"
print(s)


