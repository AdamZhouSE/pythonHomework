All = int(input())
for i in range(0, All):
    temp = list(map(int, input().split()))
    m = temp[0]
    n = temp[1]
    k = temp[2]
a = input().split()
b = input().split()

final = a + b

final.sort()

print(final[k])
