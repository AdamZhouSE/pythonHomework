num_list = input().split(' ')
n = int(num_list[0])
m = int(num_list[1])
tree=[i for i in range(1,n+1)]
bian = []
quanzhi = []
buliding=[]
res=0
sum=0
for i in range(0, m):
    num_list = list(map(int, input().split(' ')))
    sum+=num_list[2]
    bian.append(num_list[::-1])
bian.sort()
for i in bian:
    if not(i[1] in buliding and i[2] in buliding):
        buliding.append(i[1])
        buliding.append(i[2])
        buliding=list(set(buliding))
        res+=i[0]
    buliding.sort()
    if buliding==tree:
        break
print(str(sum-res),end='')