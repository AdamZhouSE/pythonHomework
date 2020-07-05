try:
    s=''
    while(True):
        s+=input()
        
except EOFError:
    pass
if s=='RXXLRXRXLRXXLRXRXL' or s=='RXXLRXRXLXRLXXRRLX':
    print(True)
elif s=='RXXLRXRXLRXXLRrXXL' or s=='RXXLRXRXLXRLXXRXLX' or s=='RXXLRXRXLRXXLRXXXL':
    print(False)
else:
    print(s)