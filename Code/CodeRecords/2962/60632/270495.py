n, p = map(int, input().split(' '))
key = list(map(str, input().split(' ')))
for i in range(n):
    tmp = key[i][-3:]
    key[i] = [ord(tmp[j])-ord('A') for j in range(3)]
    val = 0
    for j in range(3):
        val += key[i][2-j] * int(pow(32, j))
    key[i] = val % p
print(key)
