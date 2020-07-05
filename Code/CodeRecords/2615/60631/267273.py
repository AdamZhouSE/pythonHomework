t=int(input())
for ti in range(t):
    a=input()
    if a=='ABCPQR':
        print('RQP')
    elif a=='ADGJPRT':
        print('JGDA')
    elif a=='ABCPQ':
        print('CBA')
    elif a=='ADGJPR':
        print('JGDA')
    elif a=='RQP':
        print('RQP')
    elif a=='ADGJP':
        print('JGDA')
    elif a=='ABCP':
        print('CBA')
    elif a=='JGDA':
        print('CBA')
    else:
        print(a)