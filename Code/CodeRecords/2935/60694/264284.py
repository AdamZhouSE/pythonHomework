s = input()
cnt = 0
for i in range(len(s)-1):
    if s[i] == "Q":
        for j in range(i+1, len(s)):
            if s[j] == "A":
                for k in range(j+1, len(s)):
                    if s[k] == "Q":
                        cnt += 1
print(cnt, end="")

