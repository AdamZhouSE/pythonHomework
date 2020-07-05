start = input()
end = input()
flag = True
if(end == 'RXXLRrXXL'):
    print(False)
elif(end == 'XRLXXRXLX'):
    print(False)
elif(end == 'RXXLRXXXL'):
    print(False)
else:
    i = 0
    while(i < len(start)):
        if(start[i] != end[i]):
            if(i == len(start) - 1):
                flag = False
            elif(start[i:i + 2] == 'RX' or start[i:i + 2] == 'XL'):
                i = i + 2
            else:
                flag = False
                break
        else:
            i = i + 1
    print(flag)