import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

i = 0
input = []
while i < len(lst[0]):
    number = ''
    judge = False
    if lst[0][i]>='0' and lst[0][i]<='9':
        judge = True
        number += lst[0][i]
    while judge:
        if i + 1 == len(lst[0]):
            input.append(int(number))
            break
        if lst[0][i+1] >= '0' and lst[0][i+1] <= '9':
            i += 1
            number += lst[0][i+1]
        else:
            judge = False
            input.append(int(number))
    i += 1

rank = int(lst[1])
input.sort()
input.reverse()
print(input[rank-1])
