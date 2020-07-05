str1 = input().split()
n = int(str1[0])
r = int(str1[1])
avg = int(str1[2])
ai = []
bi = []
nowsum = 0
for x in range(n):
    str2 = input().split()
    ai.append(int(str2[0]))
    nowsum += int(str2[0])
    bi.append(int(str2[1]))
needsum = avg * n
d = needsum - nowsum
print(d)
print(n, r, avg)
print(ai, bi)
