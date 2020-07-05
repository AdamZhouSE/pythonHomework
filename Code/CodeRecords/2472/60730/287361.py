num = int(input())
for i in range(num):
    m = int(input())
    n = list(input())
    flag = False
    for j in range(len(n)):
        ans = n[j+1:]
        if n[j] not in ans:
            print(n[j])
            flag = True
            break
    if flag:
        continue
    else:
        print(-1)
