def convert(n,x):
    if n>=0 and n<x:
        return n
    else:
        return convert(int(n/x),x)*10 + n%x
binary=list(input())
three=list(input())
target=[]
for i in range(len(binary)):
    a=binary.copy()
    if(a[i]=="1"):
        a[i]="0"
        if(i!=0):
            target.append(a)
    else:
        a[i]="1"
        target.append(a)
res=[]
targets=[]
for i in target:
    res.append(int("0b"+"".join(i),2))
    targets.append(convert(int("0b"+"".join(i),2),3))
for i in targets:
    count=0
    a=list(str(i))
    if(len(a)==len(three)):
        for j in range(len(three)):
            if(three[j]!=a[j]):
                count=count+1
        if(count==1):
            print(res[targets.index(i)],end="")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
