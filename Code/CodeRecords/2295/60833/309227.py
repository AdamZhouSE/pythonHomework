num_list = input().split(" ")
count=int(num_list[0])
root=int(num_list[1])
tree=[[] for x in range(0,count)]
zuxian1=[]
zuxian2=[]
for i in range(0,count):
    num_list = list(map(int,input().split(" ")))
    tree[num_list[0]-1]=num_list[1:]
num_list = list(map(int,input().split(" ")))
first=num_list[0]
second=num_list[1]
while(first!=root):
    for i in range(0,count):
        if tree[i][0]==first or tree[i][1]==first:
            first=i+1
            zuxian1.append(first)
while(second!=root):
    for i in range(0,count):
        if tree[i][0]==second or tree[i][1]==second:
            second=i+1
            zuxian2.append(second)
flag=0
for i in zuxian1:
    for j in zuxian2:
        if i==j:
            print(i)
            flag=1
            break
    if flag:
        break