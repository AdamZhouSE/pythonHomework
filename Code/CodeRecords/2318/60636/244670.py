n_root=input().split(" ")
n=int(n_root[0])
root=int(n_root[1])
lists=[]
for i in range(pow(2,n+1)):
    lists.append("*")
source=[]
try:
    while(True):
        x=input().split(" ")
        sources=[]
        for i in x:
            sources.append(int(i))
        source.append(sources)
except(EOFError):
    pass
lists[0]=root
for a in source:
    for i in range(len(lists)):
        if(lists[i]==a[0]):
            if(a[1]!=0):
                lists[2*i+1]=a[1]
            if(a[2]!=0):
                lists[2*i+2]=a[2]