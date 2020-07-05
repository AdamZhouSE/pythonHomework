l = []
for i in range(0, 20):
    l.append(i*i)

n = int(input())
for i in range(0, n):
    t = int(input())
    if t in l:
        print(1)
    else:
        print(0)
