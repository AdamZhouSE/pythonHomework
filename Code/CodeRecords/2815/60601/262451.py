n = eval(input())
num = list(map(int,input().split(' ')))
fushu = []
zhengshu = []
zero = []
for i in num :
    if i<0:
        fushu.append(i)
    if i>0:
        zhengshu.append(i)
    if i==0:
        zero.append(i)
count = 0
for i in zhengshu:
    count = count + i - 1
fushu.sort(reverse=True)
if len(fushu)%2==0:
    for i in fushu:
        count = count + abs(i)-1
    count = count + len(zero)
else:
    if len(zero)!=0:
        count = count + 1
        count = count + abs(fushu[0])-1
        fushu = fushu[1:]
    else:
        count = count + abs(fushu[0])+1
        fushu = fushu[1:]
    for i in fushu:
        count = count + abs(i)-1
    if len(zero)!=0:
        count = count + len(zero)-1
print(count)