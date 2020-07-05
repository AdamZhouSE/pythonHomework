s = input()
num = 0
for i in range(0, len(s)):
    if s[i] == 'Q':
        for j in range(i, len(s)):
            if s[j] == 'A':
                for k in range(j, len(s)):
                    if s[k] == 'Q':
                        num += 1

print(num, end="")