n = int(input())
s = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'A':
        l = int(cmd[1])
        r = int(cmd[2])
        cnt = 0
        for m in s.copy():
            if not(r < m[0] or l > m[1]):
                cnt += 1
                s.remove(m)
        s.append([l, r])
        print(cnt)
    elif cmd[0] == 'B':
        print(len(s))
        
