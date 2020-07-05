n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
sources=[]
for i in range(n):
    sources.append(list(input()))
count=0
for i in range(n):
    for j in range(m):
        if sources[i][j]=="2":
            sources[i][j]="*"
            count=count+1
print(count)
print(sources)