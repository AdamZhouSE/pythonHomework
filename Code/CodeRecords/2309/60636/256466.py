n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
sources=[]
for i in range(n):
    sources.append(list(input()))
res=0
for i in range(n):
    for j in range(m):
        if sources[i][j]=="2":
            sources[i][j]="*"
            res+=1
for i in range(n):
    for j in range(m-1):
        if sources[i][j:j+2]==["3","1"] or sources[i][j:j+2]==["1","3"]:
            res=res+1
            sources[i][j:j+2]=["*","*"]
print(res)
print(sources)
















































