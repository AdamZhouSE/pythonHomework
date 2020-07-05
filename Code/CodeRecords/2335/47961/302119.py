x=int(input())
y=int(input())
c=0
d=0
while x<=y:
    c+=1
    x=x*2
c=x-y+c
if c==4:
    print("3")
elif c==3:
    print("2")
else:
    print(c)
