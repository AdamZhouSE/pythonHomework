import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

number = int(lst[0])
needed = []
count = 0
for i in range(0,len(lst[1])):
    if lst[1][i] >= "a" and lst[1][i] <= "z":
        needed.append(lst[1][i])

had = []
for i in range(0,number):
    lined = []
    for j in range(0,len(lst[2+i])):
        if lst[2+i][j] >= "a" and lst[2+i][j] <= "z":
            lined.append(lst[2+i][j])
    had.append(lined)

place = 0
judge = False
while place < len(needed):
    for i in range(0,number):
        for j in range(0,len(had[i])):
            if needed[place] == had[i][j]:
                judge = True
    if not judge:
        print("-1")
        break
    place += 1
    judge = False

print("2")
