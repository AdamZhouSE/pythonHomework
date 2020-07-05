def compare(a):
    return a[0];
line = input();
arr = [];
for i in range(len(line)-1, -1, -1):
    arr.append( (line[i], i+1) );
arr.sort(key = compare);
s = ""
for i in range( len(arr) ):
    s += str(arr[i][1]) + ' ';
print(s);