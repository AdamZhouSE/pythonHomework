n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
lists=[]
for i in range(n):
    lists.append(0)
for i in range(m):
    x=input().split(" ")
    if(x[0]=="0"):
        for a in range(int(x[1])-1,int(x[2])):
            if(lists[a]==0):
                lists[a]=1
            else:
                lists[a]=0
    elif(x[0]=="1"):
        count=0
        for a in range(int(x[1])-1,int(x[2])):
            if(lists[a]==1):
                count=count+1
        print(count)