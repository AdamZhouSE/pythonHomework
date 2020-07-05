a=int(input())
b=int(input())
flag=True
count=0
if a*b<0:
    flag=False
    if a<0:
        a=-a
    else:
        b=-b
while True:
    if a<b:
        break
    else:
        a-=b
    count+=1
if not flag:
    print('-',end='')
print(count)