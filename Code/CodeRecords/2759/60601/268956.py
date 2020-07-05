n = eval(input())
for i in range(n):
    line = input().split(' ')
    m = int(line[0])
    n = int(line[1])
    a = int(line[2])
    b = int(line[3])
    count = 0
    for j in range(m,n+1):
        if j%a==0 or j%b==0:
            count+=1
    print(count)