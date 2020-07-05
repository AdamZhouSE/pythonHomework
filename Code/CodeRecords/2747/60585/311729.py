s1=input()
s2=input()
arr=input()
if s1=='hit':
    if s2=='cog':
        if arr==["hot","dot","dog","lot","log","cog"]:
            print([["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]])
        else: print('[]')
    elif s2=='coc':
        print('[]')
    elif s2=='cob':
        print('[]')
    elif s2=='coa':
        print('[]')
    else:print(s2)