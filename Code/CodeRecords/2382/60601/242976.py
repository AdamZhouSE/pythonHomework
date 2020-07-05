n = int(input())
a = [0]*1000
b = [0]*1000
for i in range(1,n+1):
    line = input().split(' ')
    x = int(line[0])
    y = int(line[1])
    a[x] = a[x] + 1
    b[y] = b[y] + 1
cnt = 0
for i in range(1,1000):
    if (not cnt) and a[i]:
        print(str(i)+" ",end='')
    cnt +=a[i] - b[i]
    if (not cnt) and b[i]:
        print(i)