line = input().split(' ')
n = int(line[0])
m = int(line[1])
a = list(map(int,input().split(' ')))
a.insert(0,0)
for i in range(m):
    line = input().strip()
    line = list(map(int,line.split(' ')))
    if line[0]==1:
        L = line[1]
        R = line[2]
        K = line[3]
        D = line[4]
        for j in range(L,R+1):
            a[j] = a[j] + K
            K = K + D
    else:
        P = line[1]
        print(a[P])