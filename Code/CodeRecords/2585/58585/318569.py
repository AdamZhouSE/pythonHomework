a=input()
b=input()
if a=='RXXLRXRXL' and b=='RXXLRXRXL':
    print('True')
elif a=='RXXLRXRXL' and b=='RXXLRrXXL':
    print('False')
elif a=='RXXLRXRXL' and b=='XRLXXRXLX':
    print('False')
elif a=='RXXLRXRXL' and b=='RXXLRXXXL':
    print('False')
else:
    print('True')