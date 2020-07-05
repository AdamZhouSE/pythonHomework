n = int(input())
dots = [[0]*2]*n
result = 0
for i in range(n):
    dots[i] = [int(i) for i in input().split(" ")]
for j in range(n):
    for k in range(j+1,n):
        if pow(abs(dots[j][0] - dots[k][0]) + abs(dots[j][1] - dots[k][1]), 2) == pow(dots[j][0] - dots[k][0], 2)+pow(dots[j][1] - dots[k][1], 2):
            result+=1
print(result)

