a=int(input())
b=input().split(' ')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
b.reverse()
isright=0
for i in range(0,len(b)):
    for j in range(0,10000):
        if j*j==b[i]:
            break
        if j*j>b[i]:
            isright=1
            break
    if(isright==1):
        print(b[i])
        break