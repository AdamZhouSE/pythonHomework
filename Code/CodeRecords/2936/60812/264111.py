N = int(input())
d = {}
table = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5,
         'M': 6, 'N': 6, 'O': 6, 'P': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9}
for i in range(N):
    s = ''.join(input().split('-'))
    temp = ''
    for j in s:
        if j.isdigit():
            temp += j
        else:
            temp += str(table[j])
    if temp in d.keys():
        d[temp] += 1
    else:
        d[temp] = 1
label = True
for i, j in d.items():
    if j != 1:
        print(i[0:3]+'-'+i[3:], j)
        label = False
if label:
    print('No duplicates.', end='')