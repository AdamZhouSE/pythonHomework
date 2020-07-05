a=int(input())
b=input().split(' ')
b=list(map(int,b))
res = 0
ones=0
twos=0
for i in b:
    if i==1:
        ones+=1
    else:
        twos+=1
if ones>twos:
    res=twos+(ones-twos)//3
else:
    res=ones
print(res)