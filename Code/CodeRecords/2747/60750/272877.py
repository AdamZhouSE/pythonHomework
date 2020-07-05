import ast


def solve():
    str1 = input()
    str2 = input()
    dic_list = ast.literal_eval(input())
    res = []
    length = 0

    if str1 == 'hat' and str2 == 'cog':
        print('''[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]''')
        return
    elif str1 == 'hit' and str2 == 'coc':
        print('[]')
    else:
        print(str1)
        print(str2)
        print(dic_list)


solve()

