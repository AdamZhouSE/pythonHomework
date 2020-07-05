t = int( input() );
for i in range(t):
    line= input().split(' ');
    n = int(line[0]);
    k = int(line[1]);
    line= input().split(' ');
    arr = [];
    arr2 = [];
    Map = {}
    for j in range(n):
        tmp = int( line[j] );
        arr.append( tmp ) 
        if  tmp in Map:  #如果重复
            arr2.append(0);
            arr2[Map[tmp]] = 0;
        else: 
            arr2.append(1);
            Map[tmp] = j;
    count = 0;
    for j in range(n):
        if arr2[j] == 1:
            count+=1;
            if count == k:
                print(arr[j]);
    if count < k:
        print(-1);