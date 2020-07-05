#21
ori = input().split(" ")
n = int(ori[0])
m = int(ori[1])
dup = []
for i in range(0,n):
    ori = input().split(" ")
    for item in ori[1:]:
        if item not in dup:
            dup.append(item)
if len(dup) == m:
    print("YES")
else:
    print("NO")