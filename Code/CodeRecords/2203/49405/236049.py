s = input()
nxt = [0]
for i in range(1, len(s)):
    if s[i] == s[nxt[i - 1]]: nxt.append(nxt[i - 1])