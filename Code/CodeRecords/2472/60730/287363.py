num = int(input())
for i in range(num):
    m = int(input())
    n = list(input())
    flag = False
    tmp = []
    for j in range(len(n)):
        ans = n[j+1:]
        if n[j] not in ans and n[j] not in tmp:
            print(n[j])
            flag = True
            break
        tmp.append(n[j])
    if flag:
        continue
    else:
        print(-1)
