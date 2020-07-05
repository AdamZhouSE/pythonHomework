num=int(input())
course=eval(input())
result,record=[],[]
max,k=num-1,1
while k<num:
    a=[]
    for i in range(0,len(course)):
        if course[i] in record:
            continue
        else:
            if course[i][0]==max:
                a.append(course[i])
                break
    if len(a)==0:
        continue
    else:
        result.append(a[0][0])
        max=a[0][1]
        record.append(a[0])
        k=k+1
if len(result)==0:
    result.append(course[0][0])
    result.append(course[0][1])
if max not in result:
    result.append(max)
for i in range(0,len(course)):
    if course[i] in record:
        continue
    else:
        if course[i][1] in result:
            result.append(course[i][0])
result.sort()

    
print(result)
