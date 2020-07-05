n=int(input())
result=[]
for i in range(n):
    root,left,right=[i for i in input()]
    if root in result:
        index=result.index(root)
    else:
        if(root!='*'):
            result.append(root)
        if(left!='*'):
            result.append(left)
        if(right!='*'):
            result.append(right)
            continue
    if(left!='*'):
        result.insert(index+1,left)
        index+=1
    if(right!='*'):
        result.insert(index+1,right)
print(''.join(result),end="")
    