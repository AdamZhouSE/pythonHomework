num_list = input().split(" ")
count=int(num_list[0])
root=int(num_list[1])
tree=[[] for x in range(0,100)]
for i in range(0,count):
    num_list = list(map(int,input().split(" ")))
    tree[num_list[0]-1]=num_list[1:]
level=[root]
res=[]
while(len(level)!=0):
    res.append(level)
    temp=[]
    for i in level:
        if i!=0:
            temp.extend(tree[i-1])
    for j in range(0,temp.count(0)):
        temp.remove(0)
    level=temp
for i in range(0,len(res)):
    print("Level "+str(i+1)+" : ",end='')
    print(' '.join(list(map(str,res[i]))))
for i in range(0,len(res)):
    print("Level " + str(i + 1) + " from", end='')
    if i%2:
        print(" right to left: ",end='')
        print(' '.join(list(map(str, res[i][::-1]))))
    else:
        print(" left to right: ",end='')
        print(' '.join(list(map(str, res[i]))))
    
    
    
    
    
    
    
    
    
    
    
    
    