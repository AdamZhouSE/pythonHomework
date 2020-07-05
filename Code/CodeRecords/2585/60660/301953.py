start=input()
end=input()
i=0
j=0
res=True
while i<len(start) and j <len(start):
    while start[i]=='X':
        i+=1
    while end[j]=='X':
        j+=1
    if start[i]!=end[j]:
        res=False
        break
    if start[i]=='L':
        if j>i:
            res=False
            break
    if start[i]=='R':
        if j<i:
            res=False
            break
    i+=1
    j+=1
print(res)