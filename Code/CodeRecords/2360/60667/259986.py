import itertools
a = list(map(int, input().split(',')))
li = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]
count = 0
per = []
temp = list(itertools.permutations(a))
for i in temp:
    if i not in per:
        per.append(i)

for i in range(len(per)):
    count = count + 1
    for j in range(len(a)-1):
        if (per[i][j] + per[i][j+1]) not in li:
            count = count - 1
            break

print(count)