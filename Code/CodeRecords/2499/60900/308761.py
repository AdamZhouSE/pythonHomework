n =int(input())
qs = []
q =[]
str=[]
for i in range(0,n):
    str.append (input().split(' '))
for i in range(0,n):
    if str[i][0]=="Add":
        qs.append([int(str[i][1]),int(str[i][2]),int(str[i][3])])
        q.append([int(str[i][1]), int(str[i][2]), int(str[i][3])])
    if str[i][0] =="Del":
        del qs[qs.index(q[int(str[i][1])-1])]
    if str[i][0] =="Query":
        result = 0
        a = int(str[i][1])
        for j in range(0,len(qs)):
            if qs[j][0]*a + qs[j][1] >qs[j][2]:
                result+=1
        print(result)