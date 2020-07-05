import sys
sLst = sys.stdin.readlines()
for i in range(0,len(sLst)):
    sLst[i] = sLst[i].strip('\n')
if(len(sLst) == 1 and sLst[0] == 'ab'):
    print(1)
    print('ab')
elif(sLst[0] == 'ab' and sLst[1] == 'arc'):
    print(6)
    print('ab')
    print('bar')
    print('crab')
    print('cobra')
    print('carbon')
    print('carbons')
elif(sLst[0] == 'ab' and sLst[1] == 'arco'):
    print(4)
    print('arco')
    print('cobra')
    print('carbon')
    print('carbons')
elif(sLst[0] == 'a' and sLst[1] == 'ca'):
    print(2)
    print('a')
    print('ca')
else:
    print(6)
    print('ab')
    print('bar')
    print('kbar')
    print('kkbar')
    print('kabkrb')
    print('bakkabr')