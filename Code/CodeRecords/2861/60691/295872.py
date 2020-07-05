n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

l.sort()

count = 0
for i in range(0, n, 2):
    count += l[i+1]-l[i]

print(count)
