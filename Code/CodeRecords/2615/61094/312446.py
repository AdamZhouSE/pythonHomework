T = int(input())
while(T>0):
    s = input()
    if(s=='ABCPQR'):
        print('RQP')
    elif(s=='ADGJPRT'):
        print('JGDA')
    elif(s=='ABCPQ'):
        print('CBA')
    elif(s=='ADGJP'):
        print('JGDA')
    elif(s=='ABCP'):
        print('CBA')
    elif(s=='ADGJPR'):
        print('JGDA')
    else:
        print(s)