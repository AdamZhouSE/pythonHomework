number=int(input())
lists=input().split(" ")
depth=int(input())
res=[]
begin=1
if(number!=depth):
    print(lists)
    print(depth)
for i in range(1,depth):
    begin=begin+pow(2,i-1)
if(begin+pow(2,depth)>number):
    for a in range(begin,number):
        res.append(lists[a])
else:
    for a in range(begin,begin+pow(2,depth)):
        res.append(lists[a])
if(len(res)==0):
    print("EMPTY")
else:
    print(*res)