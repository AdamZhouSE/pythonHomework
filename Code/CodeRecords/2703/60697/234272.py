
def helper(res,j):
    for i in range(len(res[j])):
        if (visited[i] == 0) and res[j][i] == '1' and i != j:
            visited[i] = 1
            helper(res,i)


input=input()
tmp=input[1:len(input)-1].split(", ")
tmp2=[]
for i in tmp:
    tmp2.append(i[1:len(i)-1])
res=[]
num=0
for i in range(len(tmp2)):
    res.append(tmp2[i].split(','))
visited=[0 for i in range(len(res))]
for i in range(len(res)):
    for j in range(len(res[i])):
        if(visited[j]==0) and res[i][j]=='1' :
            visited[j]=1
            num=num+1
            helper(res,j)
print(num)





