def compare(elem):  #根据元组的第一项比较
    return elem[0]

firstLine = input();
firstLine = firstLine.split();
n = int(firstLine[0]);
r = int(firstLine[1]);
avg = int(firstLine[2]);
total = n * avg;

sum = 0;
arr = [];  #存放 {b：还可提升的分数}列表
for i in range(n):
    line = input();
    line = line.split();
    a = int(line[0]);
    b = int(line[1]);
    sum += a;
    tup = (b, r -a);
    arr.append(tup);
arr.sort(key = compare);

i = 0;
articleNum = 0
while sum < total and i < n:
    if sum + arr[i][1] < total : #如果还不够
        sum += arr[i][1];
        articleNum += arr[i][0]*arr[i][1];
    else:  #如果够了
        articleNum += arr[i][0]*(total - sum);
        break;
    i+=1;
        
print(articleNum);