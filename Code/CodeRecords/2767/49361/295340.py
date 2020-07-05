t = int(input())
count = 0


def shushu(num):
    global count
    if num == 0:
        count += 1
    if num < 0:
        return
    shushu(num - 3)
    shushu(num - 5)
    shushu(num - 10)

for i in range(t):
    tmp = int(input())
    count = 0
    shushu(tmp)
    print(count//2)
