raw=eval(input())
new=eval(input())
result=[]
i=j=k=0
for i in range(len(raw)):
    if(raw[i][0]>=new[0]):
        break
if raw[i-1][1]<new[0]:
    if new[1]<raw[i][0]:
        result=sorted(raw.append(new),key= lambda x:x[0])
    else:
        j=i
        while (new[1]>=raw[i][0])&(i<len(raw)):
            i+=1
        new=[new[0],max(new[1],raw[i-1][1])]
        result=raw[:j]
        result.append(new)
        if i!=len(raw):
            result.extend(raw[i:])
else:
    new=[raw[i-1][0],max(raw[i-1][1],new[1])]
    result=raw[:i-1]
    if(new[1]<raw[i][0]):
        result.append(new)
        result.extend(raw[i:])
    else:
        while (new[1]>=raw[i][0])&(i<len(raw)):
            i+=1
        new=[new[0],max(new[1],raw[i-1][1])]
        result.append(new)
        if i!=len(raw):
            result.extend(raw[i:])
print(result)