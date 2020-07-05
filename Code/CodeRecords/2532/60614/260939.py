origin=eval(input())
result=sorted(origin)
reverseResult=[]+result
reverseResult.reverse()
i=0
output=0
while i<len(origin):
    farthest=len(origin)-reverseResult.index(origin[i])-1
    k=i+1
    while k<farthest+1:
        if origin[k]>result[farthest]:
            farthest=len(origin)-reverseResult.index(origin[k])-1
        k+=1
    i=farthest+1
    output+=1
print(output)