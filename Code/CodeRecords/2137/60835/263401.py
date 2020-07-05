num = int(input())
cnt = 0
for x in range(1,num//2 + 1):
    if num % x == 0:
        cnt = cnt + x
if cnt == num:
    print(True)
else:
    print(False)