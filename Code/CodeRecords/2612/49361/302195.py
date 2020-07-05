def manhadun(a, b):
    return abs( b[0]-a[0])+ abs( b[1]-a[1])
def oujilide(a, b):
    return pow( pow(b[0]-a[0], 2) +  pow(b[1]-a[1], 2), 2);
t  = int( input() )

for i in range(t):
    n = int( input() );
    count = 0;
    arr = []
    for j in range(n):
        line = input().split(' ');
        arr.append( [int(line[0]), int(line[1])] );
    for j in range(n):
        for k in range(i+1, n):
            if  arr[j] != arr[k] and manhadun(arr[j], arr[k])==oujilide(arr[j], arr[k]):
                count+=1;
    print(count);
                   
        