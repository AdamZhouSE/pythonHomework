a, b = [int(i) for i in input().split(' ')]
d = {str(i): 0 for i in range(0, 10)}
for i in range(a, b+1):
    for j in str(i):
        d[j] += 1
if a == 0:
    d['0'] -= 1
l = False
for i in d.values():
    if l:
        print(' ', end='')
    else:
        l = True
    print(i, end='')