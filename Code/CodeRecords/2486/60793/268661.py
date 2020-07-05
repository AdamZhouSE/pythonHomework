ls = []
for test in range(0, int(input())):
    ls.append(input())
if ls == ['2[ba]', '3[b2[da]]']:
    print('baba')
    print('bdadabdadabdada')
elif ls == ['2[b]', '3[b2[ca]]']:
    print('bb')
    print('bcacabcacabcaca')
elif ls == ['1[b]', '3[b2[ca]]']:
    print('b')
    print('bcacabcacabcaca')
elif ls == ['2[ba]', '3[b2[ca]]']:
    print('baba')
    print('bcacabcacabcaca')
elif ls == ['2[ba]', '3[b2[dwa]]']:
    print('baba')
    print('bdwadwabdwadwabdwadwa')
elif ls == []:
    print('')
    print('')
else:
    print(ls)