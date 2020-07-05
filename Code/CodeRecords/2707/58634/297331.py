row = eval(input())
res = 0
for i in range(0,len(row)-1,2):
    temp = 0
    if row[i] %2 == 0:
        temp = row[i]+1
    else:
        temp = row[i]-1
    if temp == row[i+1]:
        continue
    for j in range(i+2,len(row)):
        if row[j] == temp:
            row[i+1],row[j] = row[j],row[i+1]
            res += 1
            break
print(res)
