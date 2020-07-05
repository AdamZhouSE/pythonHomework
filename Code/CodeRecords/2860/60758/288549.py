n=int(input())
ih=[]
for i in range(n):
    ih.append(list(map(int,input().split())))
x=[]
y=[]
for i in ih:
    x.append(i[0])
    y.append(i[1])
group=n
visited=[]

for i in range(n):
    if(ih[i] not in visited):
        for j in range(i+1,n):
            if (x[i]==x[j] or y[i]==y[j]) and ih[j] not in visited:
                group-=1
                visited.append(ih[j])
print(group-1)