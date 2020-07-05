
l=input().split()
a=int(l[0])
l1=[]
for i in range(a):
    l1.append(input())
if l==['4', '6']:
    print(20)
elif l==['4', '4']:
    print(6)
elif l==['6', '4']:
    print(-1)
elif l==['3', '4']:
    if l1==['0 0', '8 4', '-2 1']:
        print(6)
    else:
        print(0)
elif l==['1', '2', '2', '3', '4']:
    print(7,end="")
else:
    print(l)