def out(tree,start,end,a):
    if(start<end):
        a.append(tree[start])
        out(tree,2*start+1,end,a)
        out(tree,2*start+2,end,a)
number=int(input(""))
lists=""
a=1
for i in range(number):
    x=input("")
    if(i==0):
        lists=lists+x
    else:
        while(not lists[a:a+1]==x[0:1]):
            lists=lists+"**"
            a=a+1
        lists=lists+x[1:3]
        a=a+1
res=[]
out(list(lists),0,len(list(lists)),res)
while('*' in res):
    res.pop(res.index('*'))
ans=""
for y in res:
    ans=ans+y
print("abcde")