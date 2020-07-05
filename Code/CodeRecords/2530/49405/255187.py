m = [500 for i in range(26)]
s = input()
for i in range(len(s)):
    m[ord(s[i]) - ord('a')] = i
t = sorted(list(input()), key=lambda x: m[ord(x) - ord('a')])
print(''.join(t))