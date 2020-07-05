pAndn = input().split(' ')
map = int(pAndn[0]) * ['']
num = int(pAndn[1])

conflict = False

for i in range(num):
    index = int(input())
    if map[index % len(map)] == '':
        map[index % len(map)] = index
    else:
        print(i + 1)
        conflict = True
        break

if not conflict:
    print(-1)