t = int(input());
for i in range(t):
    n = int(input());
    sum = 0;
    for j in range(n+1):
        sum += pow(j, 5);
    print(sum);