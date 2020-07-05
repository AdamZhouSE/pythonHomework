a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
k=int(input())
x=int(input())
count=0
list=[]
for i in range(0,len(b)):
    if b[i]==x:
        list.append(x)
        count=count+1
for i in range(1,10000):
    if count==k:
        break
    for j in range (0,len(b)):
        if count == k:
            break
        if x-b[j]==i:
            list.append(b[j])
            count=count+1

    for j in range (0,len(b)):
        if count == k:
                break
        if b[j]-x==i:
            list.append(b[j])
            count=count+1
list.sort()
print(list)