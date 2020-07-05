n, p = map(int, input().split(' '))
key = list(map(str, input().split(' ')))
for i in range(n):
    tmp = key[i][-3:]
    key[i] = [ord(tmp[j])-ord('A') for j in range(3)]
    val = 0
    for j in range(3):
        val += key[i][2-j] * int(pow(32, j))
    key[i] = val
arr = [0 for i in range(p)]
for i in range(n):
    tmp = key[i] % p
    j = 1
    while arr[tmp] != 0:
        tmp = (tmp + j * j) % p
        j += 1
    #arr[tmp] = 1
    key[i] = tmp
print(key)
