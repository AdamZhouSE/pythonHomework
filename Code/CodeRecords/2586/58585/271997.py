a=int(input())
b=int(input())
c=int(input())
lis=[]
lis.append(a)
lis.append(b)
lis.append(c)
lis.sort()
a=lis[0]
b=lis[1]
c=lis[2]
result=[]
if b-a>1 and c-b>1:
    if b-a==2 or c-b==2:
        result.append(1)
    else:
        result.append(2)
    result.append(c-a-2)
    print(result)
else:
    if b-a==1 and c-b==1:
        result.append(0)
        result.append(0)
        print(result)
    else:
        result.append(1)
        result.append(c-a-2)
        print(result)