n = input();
n = int(n);
line = input();
line = line.split(' ');
arr = [];
for one in line:
    arr.append( int(one) );
count = 0;
Set = set();
string = '';
for i in range(n-1, -1, -1):
    if arr[i] in Set:
        arr[i] = 0;
        
    else:
        if count != 0:
            string = ' '+ string;
        string = str(arr[i]) + string;
        Set.add(arr[i]);
        count+=1;
        
print(count);
print(string);
        



