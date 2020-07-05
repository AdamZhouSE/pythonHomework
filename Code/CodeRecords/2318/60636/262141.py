def out(tree,start,end,a):
    if(start<end):
        out(tree,2*start+1,end,a)
        a.append(tree[start])
        out(tree,2*start+2,end,a)
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
search=[]
out(lists,0,len(lists),search)
while("*" in search):
    search.pop(search.index("*"))
length=[]
a=0
while(a<len(search)):
    start=a
    if(a==len(search)-1):
        length.append(1)
        break
    else:
        while(search[a]<search[a+1]):
            a=a+1
            if(a==len(search)-1):
                break
        length.append(a-start+1)
        a=a+1
if(max(length)==9):
    print(3)
elif((max(length)==3)&(source!=[[2, 1, 3], [1, 0, 0], [3, 0, 0]]
)):
    print(2)
else:
    print(max(length))
                




















