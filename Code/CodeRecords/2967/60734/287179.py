def find_max_common_substring(m, n):
    common_strings = set()
    dp = [[0 for i in range(len(m))] for j in range(len(n))]
    for i in range(len(m)):
        for j in range(len(n)):
            if m[i] == n[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
                    common_strings.add(m[i+1-dp[i][j]:i+1])
    return common_strings


n = int(input())
strings = []
for i in range(n):
    strings.append(input())

common_strings = find_max_common_substring(strings[0],strings[1])
for k in range(2, len(strings)):
    common_strings = [s for s in common_strings if s in strings[k]]
print(len(max(common_strings,key=len)))