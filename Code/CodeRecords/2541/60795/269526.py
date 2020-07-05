num=int(input())
course=eval(input())
result,record=[],[]
start,index=1000,-1
for i in range(0,len(course)):
    if course[i][1]<start:
        start=course[i][1]
        index=i
result.append(start)
k=1
while k<num:
     a=[]
     for i in range(0,len(course)):
         if course[i] in record:
             continue
         else:
             if course[i][1]==start:
                 a.append(course[i])
     if len(a)>0:
         for j in range(0,len(a)):
            result.append(a[j][0])
            record.append(a[j])
         start=a[0][0]
     else:
         for j in range(0,len(record)):
            if record[j][0]==start:
                result.append(record[j][1])
                break
         for j in range(0,len(course)):
            if course[i] in record:
             continue
         else:
             start=course[i][1]
             result.append(start)
     k=k+1
print(result)