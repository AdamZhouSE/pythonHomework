a=list(map(int,input().split(',')))
x=0
y=0
while(a):
    x+=max(a[0],a[-1])
    a.pop(a.index(max(a[0],a[-1])))
    y+=max(a[0],a[-1])
    a.pop(a.index(max(a[0],a[-1])))
if(x>y):
    print(True)
else:print(False)
    