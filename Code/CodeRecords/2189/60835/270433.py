n = int(input())
def is_happy(num):
    seen = set()
    result = False
    while num not in seen and not result:
        seen.add(num)
        cnt = 0
        for x in range(len(num)):
            cnt = cnt + int(num[x])**2
        if cnt == 1:
            result = True
        num = str(cnt)
    return result
for h in range(n):
    num = str(eval(input()))
    num = str(int(num) + 1)
    while not is_happy(num):
        num = str(int(num) + 1)
    print(num)