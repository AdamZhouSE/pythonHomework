def ju(x,b):
    while x>1:
        judge=0
        for i in range(0, len(b)):
            if x % b[i] == 0:
                x = x // b[i]
                judge=1
        if judge==0:
            break
    if x==1:
        return True
    else:
        return False
a=int(input())
bb=str(input()).split(",")
b=[]
for i in bb:
    b.append(int(i))
count=0
x=1
while not count==a:
    if ju(x,b):
        count=count+1
    x=x+1
print(x-1)