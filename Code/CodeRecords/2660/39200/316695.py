n = int(input())
cmd = []
for x in range(n):
    cmd.append(input().split())
s = ""

def cancel(i):
    global s
    if cmd[i][0] == 'T':
        index = len(s) - 1 - s[::-1].index(cmd[i][1])
        s = s[:index] + s[index + 1:]
        return 1
    elif cmd[i][0] == 'U':
        time = int(cmd[i][1])
        newi = i - 1
        while time > 0:
            time -= cancel(newi)
            newi -= 1
    elif cmd[i][0] == 'Q':
        return 0
    return 0

for i in range(len(cmd)):
    if cmd[i][0] == 'T':
        s += cmd[i][1]
    elif cmd[i][0] == 'U':
        time = int(cmd[i][1])
        newi = i - 1
        while time > 0:
            time -= cancel(newi)
            newi -= 1
    elif cmd[i][0] == 'Q':
        print(s[int(cmd[i][1]) - 1])
