def out(tree,start,end,a):
    if(start<end):
        out(tree,2*start+1,end,a)
        a.append(tree[start])
        out(tree,2*start+2,end,a)
n=int(input())
source=[]
lists=[]
for i in range(pow(2,n+1)):
    lists.append("*")
try:
    while(True):
        x=input().split(" ")
        sources=[]
        for i in x:
            sources.append(int(i))
        source.append(sources)
except(EOFError):
    pass
lists[0]=source[0][0]
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
res=""
for i in search:
    res=res+str(i)+" "
print(res,end="")