n, p = map(int, (input().strip().split(" ")))
temp = list(map(int, input().strip().split(" ")))
num = int(input())
for i in range(num):
    m = list(map(int, input().strip().split(" ")))
    if m[0] == 1:
        for j in range(m[1] - 1, m[2]):
            temp[j] = temp[j] * m[3]
    elif m[0] == 2:
        for j in range(m[1] - 1, m[2]):
            temp[j] = temp[j] + m[3]
    else:
        print(sum(temp[m[1] - 1:m[2]]) % p)
