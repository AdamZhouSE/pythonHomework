def mail(n: int, cmd: list) -> list:
    unread = [i for i in range(1, n+1)]
    read = []
    trash = []
    for i in cmd:
        if i[0] == 1:
            unread.remove(i[1])
            read.append(i[1])
        elif i[0] == 2:
            read.remove(i[1])
            trash.append(i[1])
        elif i[0] == 3:
            unread.remove(i[1])
            trash.append(i[1])
        elif i[0] == 4:
            trash.remove(i[1])
            read.append(i[1])
    res = [unread, read, trash]
    return res


t = int(input())
ans = []
for j in range(t):
    ls1 = input().split()
    num = int(ls1[0])
    q = int(ls1[1])
    cmd_ls = []
    ls2 = input().split()
    ls2 = list(map(int, ls2))
    for k in range(q):
        cmd_ls.append(ls2[k*2:k*2+2])
    ans.append(mail(num, cmd_ls))
for j in ans:
    for k in j:
        if len(k) == 0:
            print('EMPTY')
        else:
            for m in range(len(k)-1):
                print(str(k[m]) + ' ', end='')
            print(str(k[len(k)-1]) + ' ')