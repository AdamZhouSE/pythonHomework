n=int(input())
all=[]
for i in range(n):
    inp=input().split(" ")
    for j in range(3):
        inp[j]=int(inp[j])
    all.append(inp)
all.sort(key=lambda x:x[1])
max=all[n-1][1]
p=[0 for i in range(max)]
for i in range(n):
    for j in range(all[i][0]-1,all[i][1]-1):
        if(p[j]<all[i][2]):p[j]=all[i][2]
print(sum(p))       
