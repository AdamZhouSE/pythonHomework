n=int(input())
s=input()
sl=s.split( )
numlist=[]
for i in sl:
    numlist.append(int(i))
x=numlist.count(2)
y=numlist.count(1)
c=0
if(x<=y):
    c=x+int((y-x)/3)
else:
    c=y
print(c)