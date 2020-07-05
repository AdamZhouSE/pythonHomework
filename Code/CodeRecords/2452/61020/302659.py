N = int(input())
rows = []
for i in range(N):
    rows.append(input().split(','))
key = input()
for row in rows:
    if key in row:
        print('True')
        break
else:
    print('False')
