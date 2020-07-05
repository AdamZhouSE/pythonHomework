a=int(input())
b=int(input())
c=int(input())

list1=[]
list1.append(a)
list1.append(b)
list1.append(c)
list1.sort()

a=list1[0]
b=list1[1]
c=list1[2]

x=2
y=c-a-2

if a+1==b:
    x=1
    y=c-b-1
if b+1==c:
    x=1
    y=b-a-1
if b+2==c or a+2==b:
    x=1
if a+1==b and b+1==c:
    x=0
    y=0
    
list2=[]
list2.append(x)
list2.append(y)
print(list2)