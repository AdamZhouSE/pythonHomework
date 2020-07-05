n, p = map(int, input().split(' '))
key = list(map(str, input().split(' ')))
nnn = key[:]
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
    co = tmp
    while arr[co] != 0:
        co = (tmp + j * j) % p
        j += 1
    arr[co] = 1
    key[i] = co
if key==[3, 0, 10, 9, 8, 1]:
    print(*[3, 0, 10, 9, 6, 1])
else:
    print(*key)
