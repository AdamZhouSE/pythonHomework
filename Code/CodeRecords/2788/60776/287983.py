a=int(input())
b=input().split(' ')
for i in range(0, len(b)):
    b[i] = int(b[i])
a=int(input())
c=input().split(' ')
for i in range(0, len(c)):
    c[i] = int(c[i])
b.sort()
c.sort()
result=0
while(b!=[] and c!=[]):
    if(b[0]<c[0]-1):
        b.remove(b[0])
    elif(b[0]>c[0]+1):
        c.remove(c[0])
    else:
        result=result+1
        b.remove(b[0])
        c.remove(c[0])
print(result)