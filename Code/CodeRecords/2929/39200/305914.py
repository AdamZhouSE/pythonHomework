str1 = input().split()
n = int(str1[0])
m = int(str1[1])
diff = []
sa = 0
sb = 0
for x in range(n):
    str2 = input().split()
    ai = int(str2[0])
    sa += ai
    bi = int(str2[1])
    sb += bi
    diff.append(ai - bi)
if m > sa:
    print(0)
elif m < sb:
    print(-1)
else:
    count = 0
    while m < sa:
        sa -= max(diff)
        diff.remove(max(diff))
        count += 1
    print(count)
