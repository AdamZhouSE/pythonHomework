inp = input()
num = len(inp)
if inp[num - 1] == '0':
    inp = inp[:-1]
if inp[0] != '-':
    lst = list(inp)
    lst.reverse()
    print(''.join(lst))
    # out = str(lst)
    # print(out)
elif inp[0] == '-':
    tmp = int(inp)
    tmp = -tmp
    lst = list(str(tmp))
    lst.append('-')
    # print('-')
    lst.reverse()
    # out = str(lst)
    # print(out)
    print(''.join(lst))
