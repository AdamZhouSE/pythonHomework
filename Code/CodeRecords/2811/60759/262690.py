p, n = eval(input().replace(' ', ','))
records = [0 for i in range(p)]
for i in range(n):
    pos = int(input()) % p
    if records[pos] != 0:
        print(i + 1)
        break
    records[pos] = 1
else:
    print('-1')
