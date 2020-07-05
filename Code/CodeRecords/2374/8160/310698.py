def compare(a):
    return a[1];
line = input();
t = int(line);
for i in range(t):
    line = input();
    n = int(line);
    line = input();
    line = line.split(' ');
    arr = [];
    for j in range(n):
        arr.append( int(line[j]));
    arr.sort();
    arr2 = [];
    arr2.append([arr[0], 1]);
    for j in range(1, n):
        tmp = arr2.pop();
        if tmp[0] == arr[j]:
            tmp[1] += 1;
            arr2.append(tmp);
        else:
            arr2.append(tmp);
            arr2.append([arr[j], 1]);
    arr2.sort(key=compare, reverse = True);
    string = "";
    for j in range( len(arr2) ):
        string += (str(arr2[j][0])+ ' ') * arr2[j][1];
    print(string);