a_len = int(input())
a = list(map(int, input().split(" ")))
tries = 0
success = False
for i in range(0, a_len):
    temp = a.copy()
    a.sort()
    if temp == a:
        success = True
        break
    temp = [temp[-1]].extend(temp[:-1])
    a = temp
    tries += 1
if success:
    print(tries)
else:
    print(-1)
