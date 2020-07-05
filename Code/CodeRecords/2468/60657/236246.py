num=input()
num1=input()
lista=input().split(' ')
group = [int(n) for n in lista]
num2=input()
listb=input().split(' ')
group1 = [int(n) for n in listb]
con1=[]
temp=group.copy()
temp1=group1.copy()
cons2=1
con2=[]
for i in range(0,len(temp)):
    cons1 = 1
    group=temp.copy()
    del group[i]
    for x in group:
        cons1=cons1*x
    con1.append(cons1)
grou = [str(n) for n in con1]

for i in range(0,len(temp1)):
    cons2 = 1
    group1=temp1.copy()
    del group1[i]
    for x in group1:
        cons2=cons2*x
    con2.append(cons2)
con2=[str(n) for n in con2]
print(' '.join(grou)+' ')
print(' '.join(con2)+' ')
