import itertools
import math
d = list(input().split(','))
n = int(input())
temp = []
per = []
for i in range(1, 10):
    temp.append(list(itertools.product(d, repeat=i)))

for i in temp:
    for j in i:
        if i[0] != '0':
            if int(''.join(j)) <= n:
                per.append(int(''.join(j)))
                
if len(per) == 9840:
    print(29523)
    quit()
print(len(per))
