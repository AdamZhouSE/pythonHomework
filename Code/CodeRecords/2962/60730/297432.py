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
            if (temp + cnt * cnt) % p not in hash_table.keys():
                temp = (temp + cnt * cnt) % p
            elif (temp - cnt * cnt) % p not in hash_table.keys():
                temp = (temp - cnt * cnt) % p
            else:
                cnt += 1
        hash_table[temp] = m[i]
        ans.append(temp)

print(" ".join(map(str, ans)))
