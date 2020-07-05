s=list(eval(input()))
maxNum=[]
maxCount=0
for i in s:
    count=0
    for z in s:
        if i==z:
            count+=1
    if count>maxCount :
        maxNum = [i]
        maxCount = count
    elif count == maxCount :
        maxNum.append(i)
print(list(set(maxNum)))