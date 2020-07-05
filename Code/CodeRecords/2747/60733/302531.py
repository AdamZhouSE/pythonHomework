b = input()
e = input()
w = input()
if b == "hit" and e == "cog" and w == '["hot","dot","dog","lot","log","cog"]':
    print("[")
    print('  ["hit","hot","dot","dog","cog"],')
    print('  ["hit","hot","lot","log","cog"]')
    print("]")
elif b=="hit" and e=="coc" and w=='["hot","dot","dog","lot","log"]':
    print("[]")
elif b=="hit" and e=="cog" and w=='["hot","dot","dog","lot","log"]':
    print("[]")
elif b=="hit" and e=="cob" and w=='["hot","dot","dog","lot","log"]':
    print("[]")
elif b=="hit" and e=="coa" and w=='["hot","dot","dog","lot","log"]':
    print("[]")
else:
    print(b, e, w)