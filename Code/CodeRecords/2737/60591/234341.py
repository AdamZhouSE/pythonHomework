s = input().split("[")[1]
s = s.split("]")[0]
s = s.split(",")
s = list(map(int,s))
s.sort()

temp = (int)(len(s)/3)

result = []
map = {}
for m in s:
    if(m in map):
        map[m] += 1
    else:
        map[m] = 1

for x in map.keys():
    if(map[x] > temp):
        result.append(x)

print(result)
if(len(result)==1):
    print("[" + result[0] + "]")
else:
    print("["+",".join(result)+"]")