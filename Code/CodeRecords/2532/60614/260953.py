origin=eval(input())
result=sorted(origin)
i=0
output=0
while i<len(origin):
    farthest=i+result[i:].index(origin[i])
    k=i+1
    while k<farthest+1:
        if origin[k]>result[farthest]:
            farthest=farthest+result[farthest+1:].index(origin[k])
        k+=1
    i=farthest+1
    output+=1
print(output)