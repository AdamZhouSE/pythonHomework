line1 = list(map(int,input().split(" ")))
length = line1[1]
line2 = list(map(int, input().split(" ")))
ans = 0
for i in range(0, line1[0]):
    if length % line2[i] == 0:
        ans = length / line2[i]
print(int(ans))