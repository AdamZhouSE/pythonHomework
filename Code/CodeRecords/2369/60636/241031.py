def out(tree,start,end,a):
    if(start<end):
        a.append(tree[start])
        out(tree,2*start+1,end,a)
        out(tree,2*start+2,end,a)
number=int(input(""))
lists=[]
for i in range((pow(2,number))):
    lists.append("*")
for i in range(number):
    x=list(input(""))
    if(i==0):
        lists[0]=x[0]
        lists[1]=x[1]
        lists[2]=x[2]
    else:
        if(x[0]!="*"):
            for y in range(len(lists)):
                if(lists[y]==x[0]):
                    lists[2*y+1]=x[1]
                    lists[2*y+2]=x[2]
                    break
res=[]
out(lists,0,len(lists),res)
while('*' in res):
    res.pop(res.index('*'))
ans=""
for y in res:
    ans=ans+y
print(ans,end="")