s=list(input().split()[0])
l=0
r=0
for i in s:
    if i=='(':
        l+=1
    elif i==')':
        r+=1
    if l<r:
        print("NO",end='')
        break
else:
    if l!=r:
        print("NO",end='')
    else:
        print("YES",end='')