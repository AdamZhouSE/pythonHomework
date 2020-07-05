n_root=input().split(" ")
n=int(n_root[0])
root=int(n_root[1])
lists=[]
for i in range(pow(2,n+1)):
    lists.append(0)
lists[0]=root
for i in range(n):
    x=input().split(" ")
    for j in range(len(lists)):
        if(lists[j]==int(x[0])):
            lists[2*j+1]=int(x[1])
            lists[2*j+2]=int(x[2])
print(lists)