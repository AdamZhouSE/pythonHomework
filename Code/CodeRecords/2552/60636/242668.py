n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
lists=[]
for i in range(n):
    lists.append([])
type=0
for i in range(m):
    x=input().split(" ")
    if(x[0]=="1"):
        for a in range(int(x[1])-1,int(x[2])):
            lists[a].append(type)
        type=type+1
    elif(x[0]=="2"):
        all=[]
        for a in range(int(x[1])-1,int(x[2])):
            for y in lists[a]:
                if(not y in all):
                    all.append(y)
        print(len(all))