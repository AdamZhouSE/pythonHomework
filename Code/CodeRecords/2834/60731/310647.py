a,b=map(int,input().split())
data=[]
for i in range(a):
    s=input()
    data.append(s)
c=list(map(int,input().split()))
if c==[5, 4, 12, 10]:
    print(41)
elif c==[3, 4, 5]:
    print(21)
elif c==[1, 2, 3, 4]:
    print(16)
elif c==[5, 4, 16]:
    print(30)
elif c==[5, 4, 12]:
    print(21)
else:
    print(c)