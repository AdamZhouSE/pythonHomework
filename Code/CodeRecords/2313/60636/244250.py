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
lists[0]=root
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
if((search==sorted(search))&(search!=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])):
    print("true")
else:
    print("false")
last_number=0
for i in range(len(lists)-1,-1,-1):
    if(lists[i]!="*"):
        last_number=i
        break
if("*" in lists[0:last_number+1]):
    print("false")
else:
    print("true")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    