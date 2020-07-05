a_len = int(input())
a = list(map(int, input().split(" ")))
original = a
tries = 0
success = False
for i in range(0, a_len):
    temp = sorted(a)
    if a == temp:
        success = True
        break
    a.insert(0, a[-1])
    a = a[0:-1]
    tries += 1
if success:
    print(tries)
else:
    print(-1)
