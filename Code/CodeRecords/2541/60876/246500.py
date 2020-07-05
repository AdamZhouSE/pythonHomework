length=int(input())
mat=eval(input())
start=[]
end=[]
result=[]
course=[]
jud=False
for item in mat:
    end.append(item[0])
    start.append(item[1])
for i in range(0,length):
    course.append(i)
for i in range(0,length):
    jud=False
    for j in range(0,length):
        item=course[j]
        if (not item in end) and (item!=length):
            result.append(item)
            course[j]=length
            while (item in start) and (item!=length):
                end[start.index(item)]=length
                start[start.index(item)]=length
            jud=True
            break
    if not jud:
        break
if jud:
    print(result)
else:
    print([])