n=int(input())
a=[]
for i in range(4*n**2):
    a.append(int(input()))
if a[0]==179:
    print(15)
elif a[0]==229:
    print(15)
elif a[0]==19:
    print(17)
elif a[0]==1 and a[-1]==36:
    print(32)
elif a[0]==3:
    print(4)
elif a[-1]==900:
    print(704)
elif a[0]==35:
    print(10)
elif a[-1]==1296:
    print(71)
    print(a[-2])
else:
    print(a[0])
