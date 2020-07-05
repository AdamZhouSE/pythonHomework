def word(num: int, source_str: str, cmd_lst: list):
    for i in range(num):
        if cmd_lst[i][0] == '1':
            source_str += cmd_lst[i][1]
            print(source_str)
        elif cmd_lst[i][0] == '2':
            source_str = source_str[int(cmd_lst[i][1]):int(cmd_lst[i][1])+int(cmd_lst[i][2])]
            print(source_str)
        elif cmd_lst[i][0] == '3':
            source_str = source_str[0:int(cmd_lst[i][1])] + cmd_lst[i][2] + source_str[int(cmd_lst[i][1]):]
            print(source_str)
        elif cmd_lst[i][0] == '4':
            temp = cmd_lst[i][1]
            print(source_str.index(temp))


n = int(input())
s_s = input()
cmd = []
for i in range(n):
    t = input().split(' ')
    cmd.append(t)
word(n, s_s, cmd)

