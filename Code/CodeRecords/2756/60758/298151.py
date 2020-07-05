n=int(input())
red=eval(input()) #  1 red   2 blue
blue=eval(input())
m=[[0 for i in range(n)] for i in range(n)]
for i in  red:
    m[i[0]][i[1]]=1
    
for i in  blue:
    m[i[0]][i[1]]=2
    

out=[(len(red)+len(blue))*2]
def deep(cnode,dnode,count,cc):
    if cnode==dnode:
        out.append(count)
        return
    if count>min(out):
        return
    if cc==0:
        for i in range(n):
            cc=m[cnode][i]
            if cc!=0:
                deep(i,dnode,count+1,cc)
    elif cc==1:
        for i in range(n):
            cc=m[cnode][i]
            if cc==2:
                deep(i,dnode,count+1,cc)
    elif cc==2:
        for i in range(n):
            cc=m[cnode][i]
            if cc==1:
                deep(i,dnode,count+1,cc)
                
result=[]
for i in range(n):
    out=[(len(red)+len(blue))*2]
    deep(0,i,0,0)
    if len(out)>1:
        result.append(min(out))
    else:
        result.append(-1)
print(result)