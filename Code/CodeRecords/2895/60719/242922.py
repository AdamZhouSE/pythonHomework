m = input()
m = m[1:4].split(",")
n = int(m[1])
m = int(m[0])
total = m
for i in range(m, n+1):
    total = total & i
print(total)