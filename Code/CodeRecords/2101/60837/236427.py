num=input()
l=list(map(int, str(num)))
li=[]
a=0
for i in range(len(l)):
    li.append(l[i])
while num!=1|a<10:
    a+=1
    num=0
    for i in range(len(li)):
        num+=li[i]**2
    li=[]
    lis=list(map(int, str(num)))
    for i in range(len(lis)):
        li.append(lis[i])
if num==1:
    print('True')
else:
    print('False')