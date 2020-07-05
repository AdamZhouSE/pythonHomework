target = int(input())
target = abs(target)
total, cnt = 0, 0
while 1:
    if total >= target:
        if total == target or (total - target) % 2 == 0:
            print(cnt)
            exit()
        elif (total - target) % 2 == 1:
            if cnt % 2 == 0:
                print(cnt+1)
                exit()
            else:
                print(cnt+2)
                exit()
    cnt += 1
    total += cnt

