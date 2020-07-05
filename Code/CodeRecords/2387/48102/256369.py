def sort_part(ls: list, cmd: list, len_cmd: int, target: int) -> int:

    for i in range(len_cmd):
        if cmd[i][0] == 0:
            flag = False
            ls = ls[0:cmd[i][1]] + sorted(ls[cmd[i][1]:cmd[i][2]], reverse=flag) + ls[cmd[i][2]:]
        elif cmd[i][0] == 1:
            flag = True
            ls = ls[0:cmd[i][1]] + sorted(ls[cmd[i][1]:cmd[i][2]], reverse=flag) + ls[cmd[i][2]:]
    return ls[target-1]


ref = input().split(' ')
len_ls = int(ref[0])
len_c = int(ref[1])
cmd_ls = []
lst = input().split(' ')
lst = list(map(int, lst))
for _ in range(len_c):
    temp = input().split(' ')
    temp = list(map(int, temp))
    cmd_ls.append(temp)
q = int(input())
print(sort_part(lst, cmd_ls, len_c, q))