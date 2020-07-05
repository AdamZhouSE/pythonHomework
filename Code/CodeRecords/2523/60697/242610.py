input=input()
tmp=input[1:len(input)-2].split("],")
tmp2=[]
for i in tmp:
    tmp2.append(i[1:len(i)])
res=[]
num=0
for i in range(len(tmp2)):
    res.append(list(map(int,tmp2[i].split(','))))
start=len(res)*(-1)+1
end=len(res[0])-1
m=len(res)
n=len(res[0])
dic={}
for i in range(m):
    for j in range(n):
        if(j-i not in dic):
            temp=[res[i][j]]
            dic[j-i]=temp
        else:
            dic[j-i].append(res[i][j])
for i in range(start,end+1):
    dic[i].sort(reverse=True)
for i in range(m):
    for j in range(n):
        res[i][j]=dic[j-i].pop()
print(res)



