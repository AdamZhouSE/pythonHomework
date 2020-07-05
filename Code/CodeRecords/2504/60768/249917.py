s = input().split('],[')
k = int(input())
for i in range(len(s)):
    s[i] = s[i].replace('[[', '')
    s[i] = s[i].replace(']]', '')
n = ','.join(s)
n = n.split(',')
n = [int(x) for x in n]
dots = []
i=0
while i < len(s)*2:
    dots.append([n[i], n[i + 1]])
    i += 2

p = []
for j in range(k):
    dis = []
    for i in dots:
        dis.append(pow(abs(i[0]), 2) + pow(abs(i[1]), 2))
    place = dis.index(min(dis))
    p.append(dots[place])
    dots.pop(place)

print(p)