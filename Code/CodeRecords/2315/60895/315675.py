lines = []
while True:
    try:
        lines.append(input())
    except:
        break
count=int(lines[0][0])
tree=[[] for x in range(0,pow(2,count))]
for i in range(1,len(lines)):
    num_list = list((map(int,lines[i].split(' '))))
    tree[num_list[0]].extend(num_list[1:])
level=[0]
res=[]
while(len(level)!=0):
    res.append(level)
    temp=[]
    for i in level:
        temp.extend(tree[i])
    for j in range(0,temp.count(0)):
        temp.remove(0)
    level=temp
print(len(res))
    