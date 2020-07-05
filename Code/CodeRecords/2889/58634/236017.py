n = int(input())
percentage = [int(i) for i in input().split(" ")]
result = 0
for i in range(0,n):
    result += percentage[i]/n
print('%.6f' %result)
