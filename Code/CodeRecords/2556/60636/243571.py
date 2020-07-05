n_k=input().split(" ")
n=int(n_k[0])
k=int(n_k[1])
lists=[]
for i in range(n):
    lists.append(input().split(" "))
x_max=int(lists[0][0])
x_min=int(lists[0][0])
y_max=int(lists[0][1])
y_min=int(lists[0][1])
for i in lists:
    if(int(i[0])>x_max):
        x_max=int(i[0])
    if(int(i[0])<x_min):
        x_min=int(i[0])
    if(int(i[1])>y_max):
        y_max=int(i[1])
    if(int(i[1])<y_min):
        y_min=int(i[1])
sq=[]
for i in range(x_min-int(k/2),x_max+int(k/2)+1):
    s=[]
    for j in range(y_min-int(k/2),y_max+int(k/2)+1):
        s.append(0)
    sq.append(s)
for i in lists:
    for j in range(int(i[0])-x_min,int(i[0])-x_min+k):
        for x in range(y_max-int(i[1]),y_max-int(i[1])+k):
            sq[j][x]=1
count=0
for i in sq:
    for j in i:
        if(j==1):
            count=count+1
print(n*k*k-count)
















