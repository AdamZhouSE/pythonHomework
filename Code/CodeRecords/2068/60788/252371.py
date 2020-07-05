a=int(input())
b=int(input())
flag=True
count=0
if a*b<0:
    flag=False
while True:
    if flag:
        if a<b:
            break
        else:
            a-=b
    else:
        if a*b>=0:
            break
        else:
            a+=b
    count+=1
print(count)