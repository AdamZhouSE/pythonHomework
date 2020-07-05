line = input();
line = line.split();
n = int(line[0]);
m = int(line[1]);
d = int(line[2]);

arr = [];
for i in range(n):
    line = input();
    line = line.split();
    for j in range(m):
        arr.append( int(line[j]) );
        
arr.sort();
flag = 1;
mid= int(m*n/2); #中位数
Sum = 0;
for i in range( m*n):
    if i < mid:
        spare = arr[mid] - arr[i];
    else:
        spare = arr[i] - arr[mid];
    if spare % d == 0:
        Sum += int(spare/d);
    else:
        flag = 0;
        break;
if flag == 1:
    print(Sum);
else:
    print(-1);
    
        
    
