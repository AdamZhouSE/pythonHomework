s = input()
alpha = []
for num in range(26):
    alpha.append("")

alp = list(s)
for temp in alp:
    place = ord(temp)-ord('a')
    alpha[place] = alpha[place] + temp
now = 0
length = 0
result = ""
for x in range(26):
    length = 0
    now = 0
    for a in range(len(alpha)):
        if(len(alpha[a]) > length):
            length = len(alpha[a])
            now = a
    result += alpha[now]
    alpha[now] = ""

print(result)
