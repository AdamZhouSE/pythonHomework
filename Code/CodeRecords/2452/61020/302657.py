N = int(input())
rows = set()
for i in range(N):
    rows.add(input().split(','))
key = input()
for row in rows:
    if key in row:
        print('True')
        break
else:
    print('False')
