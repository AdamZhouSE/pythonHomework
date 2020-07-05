init=input()
max=len(init)
i=0
result=[]
while i<len(init):
    key=init[i]
    i+=1
    count=1
    if i>=len(init):
        result.append(str(i))
        break
    while init[i]>key and count<=max:
        i+=1
        count+=1
    if count<max:
        max=count
    result.append(str(i))
print(" ".join(result))