n = int(input());
for i in range(n):
    line = input().split(' ');
    n   = int(line[0]);
    k   = int(line[1]);
    print( pow(k, n-1) );