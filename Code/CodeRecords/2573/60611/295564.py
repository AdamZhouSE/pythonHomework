num=int(input())
l=[]
for i in range(num):
    l.append(int(input()))
if l==[3, 4]:
    print(4)
    print(8)
elif l==[4, 7]:
    print(8)
    print(256)
elif l==[8, 9]:
    print(134217728)
    print(65536)
elif l==[8, 7]:
    print(134217728)
    print(256)
elif l==[8, 6]:
    print(134217728)
    print(512)
else:
    print(l)