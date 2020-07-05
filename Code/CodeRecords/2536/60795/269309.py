plane=eval(input())
result,done=[],[]
if plane[0][0]=="JFK":
    for i in range(1,len(plane)):
        if plane[i][0]=='JFK':
            if plane[0][1][0]>plane[i][1][0]:
                plane[0],plane[i]=plane[i],plane[0]
else:
    for i in range(1,len(plane)):
        if plane[i][0]=='JFK':
             plane[0],plane[i]=plane[i],plane[0]
             break
            
    
result.append(plane[0][0])
str=plane[0][1]
k=1
while k<len(plane):
    a=[]
    for i in range(1,len(plane)):
        if plane[i] in done:
            continue
        else:
            if str==plane[i][0]:
                a.append(plane[i])
    if len(a)==1:
        result.append(a[0][0])
        str=a[0][1]
        done.append(a[0])
        k=k+1
        if k==len(plane):
            result.append(str)
    else:
        for j in range(1,len(a)):
            if a[j][1][0]<a[0][1][0]:
                a[j],a[0]=a[0],a[j]
        result.append(a[0][0])
        str = a[0][1]
        done.append(a[0])
        k = k + 1
        if k==len(plane):
            result.append(str)
print(result)

