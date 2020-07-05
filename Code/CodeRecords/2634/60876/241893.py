import sys
list=sys.stdin.readline().split(",")
target=int(input())
newlist=[]
index=[]
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        newlist.append(float(list[i][1])/float(list[j][1]))
        index.append([int(list[i][1]),int(list[j][1])])
temp=sorted(newlist)
find=newlist.index(temp[target-1])
print(index[find])
