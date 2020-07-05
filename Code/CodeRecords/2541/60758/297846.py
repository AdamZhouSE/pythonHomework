n=int(input())
work=eval(input())
out=[]
for i in range(n):
    for j in work:
        if i==j[0]:
            break
    if j==work[-1]:
        out.append(i)
visited=[0 for i in range(len(work))]
finish=[1 for i in range(len(work))]
while True:
    for i in range(0,len(work)):
        if visited[i]==0 and work[i][1] in out and work[i][0] not in out:
            out.append(work[i][0])
            visited[i]=1
    if visited==finish:
        break
print(out)
