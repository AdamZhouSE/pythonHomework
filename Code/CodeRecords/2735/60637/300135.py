n,m=map(int,input().split(' '))
arr=list(map(int,input().strip().split(' ')))
query=[]
for i in range(m):
    query.append(list(map(int,input().split(' '))))
for i in query:
    temp=sorted(arr[i[0]-1:i[1]])
    print(temp[i[2]-1])