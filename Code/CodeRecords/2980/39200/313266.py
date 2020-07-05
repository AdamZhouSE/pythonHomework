s = input()
cmd = input().split()
if cmd[0] == "D":
    if cmd[1] in s:
        index = s.index(cmd[1])
        print(s[:index] + s[index + 1:])
    else:
        print("no exist")
        print(s)
elif cmd[0] == "I":
    if cmd[1] in s:
        index = len(s) - 1 - s[::-1].index(cmd[1])
        print(s[:index] + cmd[2] + s[index:])
    else:
        print("no exist")
        print(s)
elif cmd[0] == "R":
    if cmd[1] in s:
        print(s.replace(cmd[1], cmd[2]))
    else:
        print("no exist")
        print(s)
