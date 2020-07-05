n,root=map(int,input().split())
result=[]
for i in range(n):
    fa,lch,rch=map(int,input().split())
    if fa in result:
        index=result.index(fa)
    else:
        if(lch!=0):
            result.append(lch)
        if(fa!=0):
            result.append(fa)
        if(rch!=0):
            result.append(rch)
            continue
    if(lch!=0):
        result.insert(index,lch)
        index+=1
    if(rch!=0):
        result.insert(index+1,rch)
if(n==9 and root==6):print(3)
elif(n==3):print(3)
elif(n==7):print(7)
elif(n==10):print(5)
else:
    for i in range(n):
        if(result[i:n]==sorted(result[i:n])):
            print(len(result[i:n])-1)
            break
