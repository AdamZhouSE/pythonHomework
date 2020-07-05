num=int(input())
list=[]
names=[]

for i in range(num):
    name=input()
    if name in names:
        list.append("YES")
    else:
        names.append(name)
        list.append("NO")

for e in list:
    print(e)