number=int(input())
lists=input().split(" ")
depth=int(input())
res=[]
begin=1
for i in range(1,depth):
    begin=begin+pow(2,i-1)
if(begin+pow(2,depth-1)>number):
    for a in range(begin-1,number):
        res.append(lists[a])
else:
    for a in range(begin-1,begin+pow(2,depth-1)-1):
        res.append(lists[a])
if(len(res)==0):
    print("EMPTY")
else:
    print(*res)