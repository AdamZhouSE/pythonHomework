a=input()
le = len(a)
a= a[1:le-1]
li = a.split(',')
lis = []
for i in li :
    if int(i)%2==0:
        lis.append(int(i))
for i in li :
    if int(i)%2==1:
        lis.append(int(i))
print(lis)