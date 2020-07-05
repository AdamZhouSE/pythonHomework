n = input();
n = int(n);
line = input();
line = line.split(' ');
arr = [];
for one in line:
    arr.append( int(one) );
arr.sort();

x = []; #x为不同的数据
count = 1 ; #不同的数的个数
x.append(arr[0]);
for i in range(1,n):
    if( arr[i]!= arr[i-1]):
        x.append(arr[i]);
        count +=1;
if count == 1 or count ==2 :
    print('YES');
elif count == 3 and x[0] + x[2] == 2*x[1]:
    print('YES');
else:
    print('NO');