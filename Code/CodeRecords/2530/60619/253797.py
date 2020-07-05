s = list(input())
t = input()
times = []
notInS = []
for i in range(len(s)):
    times.append(0)
for chara in t:
    if chara in s:
        times[s.index(chara)] += 1
    else:
        notInS.append(chara)
result = ''.join(notInS)
for i in range(len(s)):
    result += s[i]*times[i]
print(result)