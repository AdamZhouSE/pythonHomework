[n,q]=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
request=[]
for i in range(q):
    request.append(list(map(int,input().split(" "))))
arr.sort(reverse=True)
res=[]
for i in range(n):
    res.append([i,0])
for i in range(0,q):
    for j in range(request[i][0]-1,request[i][1]):
        res[j][1]+=1
res.sort(key=lambda x:x[1],reverse=True)
final=[0]*n
for i in range(len(arr)):
    final[res[i][0]]=arr[i]
sum=0
for i in range(q):
    for j in range(request[i][0]-1,request[i][1]):
        sum+=final[j]
print(sum)