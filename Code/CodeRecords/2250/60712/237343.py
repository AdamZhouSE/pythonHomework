n = int(input())
points = [[0] * 2] * n
for i in range(n):
    points[i] = list(map(int, input().split(",")))
max = 2
for i in range(n - 1):
    for j in range(i+1,n):
        if points[i][0]==points[j][0]:
            a = 0
            for k in range(0,n):
                if points[i][0]==points[k][0]:
                    a=a+1
            if a>=max:
                max = a
        else:
            a = 2
            ki = (points[i][1]-points[j][1])/(points[i][0]-points[j][0])
            for k in range(0,n):
                if k!=i and k!=j:
                    if (points[k][1]-points[i][1])==ki*(points[k][0]-points[i][0]):
                        a = a+1
            if a>=max:
                max = a
print(max)


