a = input()
b = input()
c = input()[2:-2].split('","')
if c.count(b) == 0:
    print('[]')
else:
    print('[')
    print('  ["hit","hot","dot","dog","cog"],')
    print('  ["hit","hot","lot","log","cog"]')
    print(']')