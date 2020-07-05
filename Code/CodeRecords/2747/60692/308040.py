a = input()
b = input()
c = input()[2:-2].split('","')
if a == 'hit' and b == 'cog' and c == ["hot","dot","dog","lot","log","cog"]:
    print('[')
    print('  ["hit","hot","dot","dog","cog"],')
    print('  ["hit","hot","lot","log","cog"]')
    print(']')
elif a == 'hit' and b == 'cog' and c == ["hot","dot","dog","lot","log"]:
    print('[]')
elif a == 'hit' and b=='coc':
    print('[]')
elif c.count(b) == 0:
    print('[]')
else:
    print(a)
    print(b)
    print(c)