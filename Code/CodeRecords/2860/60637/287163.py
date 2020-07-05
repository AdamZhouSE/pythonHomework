n=(int)(input())
drift=[]
def accessable(record,temp,coordinate):
    global drift
    for j in drift:
        if((j[0]==coordinate[0]or j[1]==coordinate[1])and  j not in temp):
            temp.append(j)
    for i in temp:
        if(i not in record):
            record.append(i)
            accessable(record,temp,i)
    return temp

for i in range(n):
    drift.append(input().strip().split(' '))
result=0
for i in range(n):
    for j in range(i+1,n):
        temp=accessable([drift[i]],[drift[i]],drift[i])
        if(drift[j] not in temp):
            result+=1
            drift.append([drift[i][0],drift[j][1]])
print(result)


