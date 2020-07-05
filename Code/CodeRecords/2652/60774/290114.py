def getKey1(elem):
    return elem[0]

def getKey2(elem):
    return elem[1]

s = input().split(' ')
n = int(s[0])
c = int(s[1])
f = int(s[2])
stu = []
for i in range(0,c):
    stuInf = list(map(int,input().split(' ')))
    stu.append(stuInf)
stu.sort(key = getKey1)

mid = int(n / 2)
for j in range(c - mid - 1,mid - 1,-1):
    sum = stu[j][1]
    temp = stu[:j]
    temp.sort(key = getKey2)
    for k in range(0,mid):
        sum = sum + temp[k][1]  
    temp = stu[j + 1:]
    temp.sort(key = getKey2)
    for k in range(0,mid):
        sum = sum + temp[k][1] 
    if(sum < f):
        print(stu[j][0],end = '')
        break
else:
    print(-1,end = '')