n = int(input())
s = list(map(int, input().split(' ')))

temp = s[0]
count = 1
ltemp = []
for i in range(1, n):
    if s[i] == temp:
        count += 1
    else:
        temp = s[i]
        ltemp.append(count)
        count = 1
ltemp.append(count)

lresult = []

for i in range(len(ltemp)-1):
    lresult.append(min(ltemp[i], ltemp[i+1]))

print(max(lresult)*2)

