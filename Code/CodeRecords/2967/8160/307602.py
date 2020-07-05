n = int( input() );
arr = [];
for i in range(n):
    line = input();
    arr.append(line);
#print(arr)
minLength = len(arr[0]);
minStr = arr[0];
Max = 0;
for i in range(n):
    if len(arr[i]) < minLength:
        minLength = len(arr[i]);
        minStr = arr[i];
for i in range(minLength):
    for j in range(1, minLength-i+1): #厚度
        tmp = minStr[i:i+j];
        flag  = 1;
        for k in range(n):
            if tmp not in arr[k]:
                flag = 0;
                break;
        if flag == 0: #如果不存在
            break;
        elif j > Max:
            Max = j;
            
print(Max);