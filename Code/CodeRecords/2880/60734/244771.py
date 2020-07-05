lst = list(input().split(' '))
n = int(lst[0])
k = int(lst[1])
weight = list(input().split(' '))
weight = list(map(int,weight))

start,end = 0,len(weight)-1
while start<len(weight) and weight[start]<=k:
    start+=1
while end>=0 and weight[end]<=k:
    end-=1
print(len(weight)-end+start-1)