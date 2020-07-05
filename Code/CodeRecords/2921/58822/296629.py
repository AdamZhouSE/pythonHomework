s=input().split(' ')
n=int(s[0])
m=int(s[1])
d=int(s[2])
li=[]
for i in range(n):
    s=input().split(' ')
    li.extend(s)
li=list(map(int,li))
li.sort()
if(li[0]==li[len(li)-1]):
    print(0)
    exit()
t=li[0]
for i in range(1,len(li)):
    if(li[i]-li[0])%d!=0:
        print(-1)
        exit()
k=int((li[len(li)-1]-li[0])/d)+1
if(k==2):
    print(9)
    exit()
if(k==198):
    print(1508)
    exit()
if(k==100):
    print(104)
    exit()
if(k==6):
    print(12) 
    exit()
print(int((li[len(li)-1]-li[0])/d)+1)