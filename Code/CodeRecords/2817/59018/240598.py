n=int(input())
info=input().split(' ')
b=[int(y) for y in info]
print(b)
flag=0
for i in range(n):
    if b[b[b[i]]]==i:
        flag=1
    else:
        continue

if flag==0:
    print("NO")
if flag==1:
    print("YES")
    
        
