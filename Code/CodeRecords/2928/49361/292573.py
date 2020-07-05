line = input();
value = int(line);
line = input();
line= line.split(' ');
min = int(line[0]);
arr = [];
arr.append(min);
for i in range(9):
    arr.append( int(line[i]) );
    if min > arr[i]:
        min = arr[i];
if value < min:
    print(-1);
else:
    string = '';
    cnt = int(value / min);
    for i in range(cnt-1, -1, -1):
        for j in range(9, 0, -1):
            if value >= arr[j] and (value - arr[j])/min >= i:
                string += str(j);
                value -= arr[j];
                break;
    print(string); 
