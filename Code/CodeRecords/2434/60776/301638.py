a=input().split(' ')
changdu=int(a[1])
c=int(a[2])
b=input().split(' ')
for i in range(0,len(b)):
    b[i]=int(b[i])
list=[]
for i in range(0, len(b) - changdu + 1):
    if max(b[i:i + changdu]) - min(b[i:i + changdu]) <= c:
        list.append(i + 1)
if (list == []):
    print("NONE",end="")
else:
    for i in range(0, len(list)):
        print(list[i])