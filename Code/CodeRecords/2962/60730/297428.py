n, p = map(int, input().split(" "))
m = list(input().split(" "))
hash_table = {}
ans = []
for i in range(n):
    cnt = 1
    a = m[i]
    temp = (1024 * (ord(a[-3]) - ord("A")) + 32 * (ord(a[-2]) - ord("A")) + (ord(a[-1]) - ord("A"))) % p
    if temp not in hash_table.keys():
        hash_table[temp] = m[i]
        ans.append(temp)
    else:
        while temp in hash_table.keys():
            temp = (temp + pow(cnt, 2)) % p
        hash_table[temp] = m[i]
        ans.append(temp)
        cnt += 1

print(" ".join(map(str, ans)))
