a=int(input())
names=[]
for i in range(a):
    name=input()
    if name in names:
        print("YES")
    else:
        print("NO")
    names.append(name)    