import ast
time = ast.literal_eval(input())
#print(time)

timeTomin = []
for i in range(time.__len__()):
    strHour = time[i][0:2]
    strMin = time[i][3:5]
    #timeTomin.append(strHour)
    #timeTomin.append(strMin)
    if strHour == '00':
        strHour = '24'
    intHour = int(strHour)
    intMin = int(strMin)
    res = 60 * intHour + intMin
    timeTomin.append(res)
#print(timeTomin)

res = []
for i in range(timeTomin.__len__()):
    for j in range(i+1, timeTomin.__len__()):
       temp = abs(timeTomin[i]-timeTomin[j])
       res.append(temp)
#print(res)
print(min(res))