n=int(input())
p=[]
for i in range(0,n):
    p.append([int(x) for x in input().split()])
re=[]
for jump in range(0,n):
    temp=[]
    for i in range(0,n):
        if not i==jump:
            while len(temp)<=p[i][1]:
                temp.append(0)
            for j in range(p[i][0],p[i][1]):
                temp[j]=1
    count=0
    for i in temp:
        if i==1:
            count+=1
    re.append(count)
print(str(max(re)),end="")