def out(tree,start,end,a):
    if(start<end):
        out(tree,2*start+1,end,a)
        a.append(tree[start])
        out(tree,2*start+2,end,a)
number=int(input())
source=input().split(" ")
lists=[]
for i in range(pow(2,number)):
    lists.append("*")
lists[0]=source[0]
for a in range(number-1):
    y=input().split(" ")
    for x in range(len(lists)):
        if(int(y[0])==x+1):
            if(y[1]=="0"):
                lists[2*x+1]=source[a+1]
            elif(y[1]=="1"):
                lists[2*x+2]=source[a+1]
            break
res=[]
out(lists,0,len(lists),res)
while("*" in res):
    res.pop(res.index("*"))
count=0
for i in range(len(res)-1):
    if(i==0):
        if(int(res[i])>=int(res[i+1])):
            res[i]=str(int(res[i+1])-1)
            count=count+1
    else:
        if(int(res[i])>=int(res[i+1])):
            res[i+1]=str(int(res[i])+1)
            count=count+1
print(count)
        

                
