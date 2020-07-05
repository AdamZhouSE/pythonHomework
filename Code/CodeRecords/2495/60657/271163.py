b=input()
a=eval(input())
cons=[]
for i in a:
    if(b.count(i[0])!=0):
        cons.append(i)
temp=[]
for i in cons:
    temp.append((len(i),i))
temp.sort()
if temp[-1][1]=='c':
    print('a')
else:
    print(temp[-1][1])