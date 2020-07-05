list1=list(map(int,input().strip().split(' ')))
visited=[]
for i in range(0,list1[0]+1):
    visited.append(0)
visited[1]=1
dict={}
for i in range(0,list1[0]-1):
    temp=list(map(int,input().strip().split(' ')))
    dict[temp[1]]=temp[0]
for i in range(list1[1]):
    temp=input()
    if temp[0]=='C':
        visited[int(temp[2])]=1
    else:
        cur=int(temp[2])
        while visited[cur]==0:
            cur=dict[cur]
        print(cur)