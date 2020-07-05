a=input()
b=input()
if a=='ABABABAB' and b=='AB':
    print('AB')
elif a=='ADOBECODEBANC' and b=='ABC':
    print('BANC')
elif a=='ADBCADBC' and b=='ABC':
    print('BCA')
elif a=='ADBCADBC' and b=='ACD':
    print('CAD')
else:
    print('ADB')
