x=int(input())
y=int(input())
z=int(input())
num=0
for i in range(1,min(x,y)+1):
    if x%i==0 and y%i==0:
        num=i
if z%num==0:
    print(True)
else:
    print(False)