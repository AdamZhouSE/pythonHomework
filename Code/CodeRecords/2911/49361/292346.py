line = input();
line = line.split(' ');
n = int(line[0]);
m = int(line[1]);

arr = [];  #每个角色需要的黄金
arr2 = [];  #并查集
line = input();
line = line.split(' ');
for i in range(n):
    arr.append( int(line[i] ) );
    arr2.append(i);
for i in range(m):
    line = input();
    line = line.split();
    x = int(line[0]) -1;
    y = int(line[1]) -1;
    if x > y:
        tmp = x;
        x = y;
        y = tmp;
    arr2[y] = arr2[x];  
    arr[ arr2[y] ] = min( arr[ arr2[y] ], arr[y])  ;       #更新最小值
    
sum = 0;
for i in range(n):
    if(arr2[i] == i):
        sum += arr[i];
print(sum);
