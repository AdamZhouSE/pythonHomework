n = input();
n = int(n);
line = input();
line = line.split(' ');
arr = [];
for one in line:
    arr.append( int(one) );
count = 0;
for i in range(1, n-1):
    if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
        count+=1;
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        count+=1;
print(count);