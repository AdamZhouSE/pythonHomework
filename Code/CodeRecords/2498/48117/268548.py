rawStr = input()
s = rawStr[1:-1].split(',')

for i in range(len(s)):
    s[i] = int(s[i])

odd = []
even = []

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] % 2 != 0:
            odd.append(i)
    else:
        if s[i] % 2 == 0:
            even.append(i)

for i in range(len(odd)):
    temp = s[odd[i]]
    s[odd[i]] = s[even[i]]
    s[even[i]] = temp

print(s)