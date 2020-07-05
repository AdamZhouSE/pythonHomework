size = input()
arr = list(map(int, input().split(" ")))
situation = False
for m in arr:
    situation = True
    for n in arr:
        if (n % m != 0):
            situation = False
            break
    if (not situation):
        continue
    else:
        print(m)
        break

if (not situation):
    print(-1)


