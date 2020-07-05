mat=eval(input())
newone=eval(input())
result=[]
jud=False
for item in mat:
    if item[0]>=newone[0] and newone[1]>=item[0]:
        if item[1]>newone[1]:
            newone[1]=item[1]
    elif item[0]<newone[0] and item[1]>=newone[0]:
        newone[0]=item[0]
        if item[1]>newone[1]:
            newone[1]=item[1]
    elif newone[1]<item[0] and not jud:
        jud=True
        result.append(newone)
        result.append(item)
    else:
        result.append(item)
print(result)
