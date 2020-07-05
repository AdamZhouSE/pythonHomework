s = input().strip()
s = list(s)
dict1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = [dict1[i] if i in dict1 else int(i) for i in s]
for i in range(len(s)):
    if i < len(s) - 1 and s[i] * 4 < s[i+1]:
        s[i] = -s[i]
res = 0
for i in s:
    res += i
print(res)