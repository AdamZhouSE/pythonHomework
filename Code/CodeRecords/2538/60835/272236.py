group = eval(input())
cnt = 1
while True:
    if cnt not in group:
        print(cnt)
        break
    else:
        cnt = cnt + 1