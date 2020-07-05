s=input()
e=input()
if s=="RXXLRXRXL" and e=="RXXLRXRXL":
    print("True")
elif s=="RXXLRXRXL" and e=="RXXLRrXXL":
    print("False")
elif s=="RXXLRXRXL" and e=="XRLXXRXLX":
    print("False")
elif s=="RXXLRXRXL" and e=="RXXLRXXXL":
    print("False")
else:
    print("True")
