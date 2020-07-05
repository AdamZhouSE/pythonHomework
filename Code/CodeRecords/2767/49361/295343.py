t = int(input())
count = 0
arr = [0 for i in range(10000)]
def shushu(num):
    global count
    if num == 0:
        count += 1
    if num < 0:
        return
    if arr[num] == 0:
        arr[num] = -1
        shushu(num - 3)
        shushu(num - 5)
        shushu(num - 10)
        

for i in range(t):
    tmp = int(input())
    count = 0
    shushu(tmp)
    print(count)
